#!/usr/bin/env python3
"""
Push a skill to a GitHub repository.

Creates the repo if it doesn't exist, pushes raw skill files to
skills/<name>/ and the packaged .skill file to skills/<name>.skill,
and keeps an index.json manifest up to date.

Usage:
    python github_push.py \
        --skill-path /path/to/skill-dir \
        --skill-file /path/to/skill.skill \
        --token <github_pat> \
        --owner <github_username_or_org> \
        --repo <repo_name> \
        [--branch main]
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print(json.dumps({"success": False, "error": "requests library not installed. Run: pip install requests --break-system-packages"}))
    sys.exit(1)


# ── GitHub API helpers ────────────────────────────────────────────────────────

class GitHubAPI:
    BASE = "https://api.github.com"

    def __init__(self, token: str, owner: str, repo: str, branch: str = "main"):
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        self.owner = owner
        self.repo = repo
        self.branch = branch

    def _url(self, path: str) -> str:
        return f"{self.BASE}{path}"

    def get(self, path: str) -> requests.Response:
        return requests.get(self._url(path), headers=self.headers)

    def put(self, path: str, body: dict) -> requests.Response:
        return requests.put(self._url(path), headers=self.headers, json=body)

    def post(self, path: str, body: dict) -> requests.Response:
        return requests.post(self._url(path), headers=self.headers, json=body)

    # ── Repo ──────────────────────────────────────────────────────────────────

    def repo_exists(self) -> bool:
        r = self.get(f"/repos/{self.owner}/{self.repo}")
        return r.status_code == 200

    def create_repo(self, description: str = "Team skill library") -> dict:
        body = {
            "name": self.repo,
            "description": description,
            "private": False,
            "auto_init": True,   # creates initial commit with README
        }
        r = self.post("/user/repos", body)
        if r.status_code not in (201, 422):  # 422 = already exists
            r.raise_for_status()
        time.sleep(2)  # give GitHub a moment after creation
        return r.json()

    # ── Files ─────────────────────────────────────────────────────────────────

    def get_file_sha(self, repo_path: str) -> str | None:
        """Return the blob SHA of an existing file, or None if it doesn't exist."""
        r = self.get(f"/repos/{self.owner}/{self.repo}/contents/{repo_path}?ref={self.branch}")
        if r.status_code == 200:
            return r.json().get("sha")
        return None

    def put_file(self, repo_path: str, content: bytes, message: str, sha: str | None = None) -> dict:
        """Create or update a single file. content is raw bytes."""
        body = {
            "message": message,
            "content": base64.b64encode(content).decode(),
            "branch": self.branch,
        }
        if sha:
            body["sha"] = sha
        r = self.put(f"/repos/{self.owner}/{self.repo}/contents/{repo_path}", body)
        if r.status_code not in (200, 201):
            raise RuntimeError(f"Failed to push {repo_path}: {r.status_code} {r.text[:300]}")
        return r.json()

    def push_file(self, repo_path: str, content: bytes, skill_name: str, action_label: str = "") -> str:
        """Push a file, auto-detecting create vs update. Returns 'created' or 'updated'."""
        sha = self.get_file_sha(repo_path)
        verb = "update" if sha else "add"
        label = f" [{action_label}]" if action_label else ""
        message = f"{verb}({skill_name}): {Path(repo_path).name}{label}"
        self.put_file(repo_path, content, message, sha)
        return "updated" if sha else "created"


# ── Repo initialisation ───────────────────────────────────────────────────────

README_TEMPLATE = """\
# Team Skill Library

A shared repository of Claude skills for our team.

## Structure

```
skills/
├── <skill-name>/          # Raw skill source files (SKILL.md + references/)
│   ├── SKILL.md
│   └── references/
└── <skill-name>.skill     # Packaged skill file (click to install)
index.json                 # Machine-readable skill catalog
```

## Installing a skill

1. Open the `.skill` file link for the skill you want
2. Click **Save skill** in the file card
3. The skill will be available in your next Claude session

## Adding a skill

Use the `push-skill-to-github` skill in Claude to push a new or updated skill here.
"""

def ensure_readme(api: GitHubAPI, is_new_repo: bool) -> None:
    if is_new_repo:
        # Overwrite the auto-generated README
        api.push_file("README.md", README_TEMPLATE.encode(), "repo-init", "initialize skill library")


def load_index(api: GitHubAPI) -> dict:
    r = api.get(f"/repos/{api.owner}/{api.repo}/contents/index.json?ref={api.branch}")
    if r.status_code == 200:
        data = r.json()
        content = base64.b64decode(data["content"]).decode()
        return json.loads(content)
    return {"skills": []}


def save_index(api: GitHubAPI, index: dict, skill_name: str) -> None:
    content = json.dumps(index, indent=2, ensure_ascii=False).encode()
    api.push_file("index.json", content, skill_name, "update index")


def update_index(index: dict, skill_name: str, description: str,
                 owner: str, repo: str, branch: str) -> None:
    base_url = f"https://github.com/{owner}/{repo}/blob/{branch}/skills"
    entry = {
        "name": skill_name,
        "description": description,
        "source_url": f"{base_url}/{skill_name}/SKILL.md",
        "skill_file_url": f"{base_url}/{skill_name}.skill",
        "raw_url": f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/skills/{skill_name}.skill",
    }
    skills = index.get("skills", [])
    existing = next((i for i, s in enumerate(skills) if s["name"] == skill_name), None)
    if existing is not None:
        skills[existing] = entry
    else:
        skills.append(entry)
    index["skills"] = sorted(skills, key=lambda s: s["name"])


# ── Main ──────────────────────────────────────────────────────────────────────

def collect_skill_files(skill_dir: Path) -> list[tuple[str, bytes]]:
    """
    Walk the skill directory and return (relative_path, content) pairs.
    Excludes evals/, __pycache__, *.pyc, .DS_Store.
    """
    SKIP_DIRS  = {"evals", "__pycache__", "node_modules"}
    SKIP_FILES = {".DS_Store"}
    SKIP_EXTS  = {".pyc"}

    files = []
    for p in sorted(skill_dir.rglob("*")):
        if not p.is_file():
            continue
        parts = p.relative_to(skill_dir).parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        if p.name in SKIP_FILES or p.suffix in SKIP_EXTS:
            continue
        rel = str(p.relative_to(skill_dir))
        files.append((rel, p.read_bytes()))
    return files


def extract_description(skill_dir: Path) -> str:
    """Pull the description from SKILL.md frontmatter."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ""
    text = skill_md.read_text(encoding="utf-8")
    # Simple frontmatter parse — look for description: field
    in_fm = False
    desc_lines = []
    capture = False
    for line in text.splitlines():
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            else:
                break
        if not in_fm:
            continue
        if line.startswith("description:"):
            rest = line[len("description:"):].strip()
            if rest and rest != "|":
                return rest.strip("\"'")
            capture = True
            continue
        if capture:
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and ":" not in stripped[:20]:
                desc_lines.append(stripped.lstrip())
            elif desc_lines:
                break
    return " ".join(desc_lines)[:200] if desc_lines else ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-path",  required=True, help="Path to skill directory")
    parser.add_argument("--skill-file",  required=True, help="Path to packaged .skill file")
    parser.add_argument("--token",       required=True, help="GitHub PAT")
    parser.add_argument("--owner",       required=True, help="GitHub username or org")
    parser.add_argument("--repo",        required=True, help="Repository name")
    parser.add_argument("--branch",      default="main")
    args = parser.parse_args()

    skill_dir  = Path(args.skill_path)
    skill_file = Path(args.skill_file)

    # Validate inputs
    if not (skill_dir / "SKILL.md").exists():
        print(json.dumps({"success": False, "error": f"No SKILL.md found in {skill_dir}"}))
        sys.exit(1)
    if not skill_file.exists():
        print(json.dumps({"success": False, "error": f"Packaged .skill file not found: {skill_file}"}))
        sys.exit(1)

    api = GitHubAPI(args.token, args.owner, args.repo, args.branch)

    # Read skill name from SKILL.md frontmatter
    skill_md_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    skill_name = None
    for line in skill_md_text.splitlines():
        if line.startswith("name:"):
            skill_name = line[5:].strip().strip("\"'")
            break
    if not skill_name:
        skill_name = skill_dir.name

    description = extract_description(skill_dir)

    result = {
        "success": True,
        "skill_name": skill_name,
        "repo_created": False,
        "files_pushed": [],
        "skill_file_pushed": None,
        "repo_url": f"https://github.com/{args.owner}/{args.repo}",
        "skill_dir_url": f"https://github.com/{args.owner}/{args.repo}/tree/{args.branch}/skills/{skill_name}",
        "skill_file_url": f"https://github.com/{args.owner}/{args.repo}/blob/{args.branch}/skills/{skill_name}.skill",
    }

    try:
        # Step 1: Ensure repo exists
        is_new = not api.repo_exists()
        if is_new:
            api.create_repo(description=f"Team skill library")
            result["repo_created"] = True
            ensure_readme(api, is_new_repo=True)

        # Step 2: Push raw skill source files
        source_files = collect_skill_files(skill_dir)
        for rel_path, content in source_files:
            repo_path = f"skills/{skill_name}/{rel_path}"
            status = api.push_file(repo_path, content, skill_name)
            result["files_pushed"].append({"path": repo_path, "status": status})

        # Step 3: Push packaged .skill file
        skill_bytes = skill_file.read_bytes()
        repo_skill_path = f"skills/{skill_name}.skill"
        status = api.push_file(repo_skill_path, skill_bytes, skill_name, "packaged")
        result["skill_file_pushed"] = {"path": repo_skill_path, "status": status}

        # Step 4: Update index.json
        index = load_index(api)
        update_index(index, skill_name, description, args.owner, args.repo, args.branch)
        save_index(api, index, skill_name)

    except Exception as e:
        result["success"] = False
        result["error"] = str(e)

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
