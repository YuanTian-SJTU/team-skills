---
name: push-skill-to-github
description: |
  Use this skill whenever the user wants to push, publish, share, or sync a skill
  to GitHub — for team sharing, version control, or building a team skill library.
  Trigger on: "push skill to github", "share skill with team", "publish skill",
  "sync skill to repo", "upload skill to github", "put skill on github",
  "team skill library", "skill repo". Also trigger when user says they want
  teammates to be able to install a skill they just created or updated.
---

# Push Skill to GitHub

## Purpose

Push a skill (both the raw source files and the packaged `.skill` file) to a
GitHub repository so teammates can browse, review, and install it. Handles
first-time repo initialization automatically.

## Pre-requisites

The user needs a GitHub Personal Access Token (PAT) with `repo` scope.
If they don't have one, tell them: Settings → Developer settings →
Personal access tokens → Tokens (classic) → Generate new token → check `repo`.

## Workflow

### Step 1 — Collect information

Ask the user for the following (all at once, not one by one):

1. **Skill to push**: path to the skill folder, OR name of a skill they just
   created in this session (look for it in the recent outputs)
2. **GitHub owner**: their GitHub username or organization name
3. **Repo name**: e.g. `team-skills` (will be created if it doesn't exist)
4. **GitHub PAT**: ask them to paste it, OR check `$GITHUB_TOKEN` env var first —
   if it's set, tell them and confirm they want to use it

To check for GITHUB_TOKEN:
```bash
echo ${GITHUB_TOKEN:0:4}...  # show only first 4 chars for safety
```

### Step 2 — Locate and validate the skill

Find the skill directory. Priority order:
1. If user gave a path, use it directly
2. If user gave a skill name, check common locations:
   - `/tmp/<skill-name>/`
   - `/sessions/*/mnt/outputs/<skill-name>/`
   - `/sessions/*/mnt/.claude/skills/<skill-name>/`

Validate: the directory must contain a `SKILL.md` file with valid YAML frontmatter
(name field required). If invalid, tell the user and stop.

Extract the skill name from the SKILL.md `name` field — use this as the
canonical name, not the directory name.

### Step 3 — Package the skill

Run the skill-creator packager to produce the `.skill` file:

```bash
SKILL_CREATOR=/sessions/$(ls /sessions/)/mnt/.claude/skills/skill-creator
python -m scripts.package_skill <skill-dir-path> /tmp/skill-push-staging/
```

If the packager is not available, create the `.skill` zip manually:
```bash
cd $(dirname <skill-dir-path>)
zip -r /tmp/skill-push-staging/<skill-name>.skill <skill-dir-name>/ \
    --exclude "*/evals/*" --exclude "*__pycache__*" --exclude "*.pyc"
```

### Step 4 — Push to GitHub

Run the push script:

```bash
pip install requests --break-system-packages -q

python /path/to/push-skill-to-github/scripts/github_push.py \
  --skill-path <validated-skill-dir> \
  --skill-file /tmp/skill-push-staging/<skill-name>.skill \
  --token <pat> \
  --owner <owner> \
  --repo <repo-name>
```

The script outputs a JSON result. Parse it and report to the user.

### Step 5 — Report results

On success, tell the user:
- The GitHub URL of the skill directory (link to browse files)
- The direct URL of the `.skill` file (teammates can Save skill from here)
- Whether the repo was newly created or already existed
- Whether the skill was newly added or updated

On failure, show the error message clearly and suggest fixes.

## Notes

- The PAT is never logged or stored — it's passed only as a command argument
  and lives only in process memory during the push
- If pushing an update to an existing skill, the script shows a summary of
  which files changed
- `index.json` in the repo root is kept up to date automatically — it serves
  as a machine-readable catalog of all skills in the repo
