---
name: ai-native-strategy
description: |
  Use this skill whenever a user wants to design, plan, analyze, or evaluate the technical
  strategy and architecture of an AI-native product. Trigger on any of the following:
  mentions of "AI原生产品", "AI产品架构", "AI技术战略", "AI战略规划", "模型选型",
  "RAG架构", "Agent架构", "知识图谱", "AI产品设计", "数据飞轮", "AI战略报告",
  "AI原生商业网络"; or requests to design an AI-first product from scratch; or evaluate
  technology choices for an AI product; or produce a strategy report / architecture
  document / pitch deck for an AI product for investors or executives. Also trigger when
  the user wants to record stakeholder research (CEO, investor, CTO, CPO, domain expert,
  early user interviews), or compare a new analysis against a previous version of a
  strategy document. This skill is especially valuable when the user wants to articulate
  WHY their product is transformatively AI-native rather than just AI-enhanced.
---

# AI-Native Product Technical Strategy & Architecture

## Purpose

Guide the user through a structured dialogue to design the technical strategy and
architecture of an AI-native product, then generate deliverables at multiple levels:

**Strategic deliverables** (for investors and C-suite):
- Strategy Report (.md, convertible to .docx)
- Architecture Document (.md with Mermaid diagrams)
- PPT Deck (.pptx via pptx-author skill)

**Execution-level supplements** (for development and product teams, on request):
- Technical Layer → Data Schema Draft + Orient Prompt Template + ERP Integration Checklist
- Application Layer → User Stories + Main User Flow + Notification Specification

**Stakeholder research documents**:
- Per-stakeholder interview records (CEO, investor, CTO, CPO, domain expert, seed user)
- Multi-stakeholder synthesis (alignment, tensions, gaps, layer-by-layer implications)

**Version management documents**:
- Delta Document comparing current vs. previous analysis version
- Decision Registry tracking key architectural decisions over time

The central narrative thread: **AI-native ≠ AI-enhanced.** An AI-native product
is one that would be impossible — not merely worse — without AI.

---

## Language Rule

Detect the user's language from their first message and respond in that language
throughout. All internal instructions are in English and must not appear verbatim
in any user-facing output.

---


## Project Convention

Every session operates in the context of a named project. The project ID is collected
in Step 0 (first thing in Phase 1) and governs all file naming and GitHub paths.

**File naming**: `<type>-YYYY-MM.md` (e.g., `strategy-report-2026-07.md`)
**GitHub path**: `analysis/<project-id>/YYYY-MM/<type>.md`
**Multiple projects** are fully supported — each gets its own subdirectory under `analysis/`.

At the end of any session that produces files, Claude generates a ready-to-run
`push_to_github.py` command block so the user can push everything with one copy-paste.

Reference routing for naming rules and push commands → references/05-output-templates.md

---

## Mode Detection

At the start of each session, determine the user's mode:

**Mode A — Stakeholder Research**
Triggered by: recording an interview, capturing inputs from a specific role
(CEO, investor, CTO, CPO, domain expert, early user), phrases like "记录访谈",
"投资人反馈", "用户调研".
→ Load references/06-stakeholder-research.md → enter Capture Mode.
→ After each interview, offer Synthesis Mode if multiple documents exist.

**Mode B — Architecture Design**
Triggered by: designing, planning, or analyzing an AI product strategy.
→ Run Phases 1–4 below.
→ Before Phase 1: check if stakeholder research documents were provided. If yes,
  offer to synthesize first before running diagnosis.

**Mode C — Version Comparison**
Triggered by: user uploads a previous strategy/architecture document AND signals
intent to compare ("做第二版", "对比上一版", "update last analysis", "what changed").
→ Load references/07-version-delta.md.
→ Extract Decision Registry from the uploaded document.
→ Collect what changed (AI capabilities, market feedback, competition, team).
→ Re-evaluate each decision and produce a Delta Document.
→ After the Delta Document, offer to run a full Phase 2 re-analysis on layers
  where decisions were invalidated or substantially updated.

All three modes can run within the same session and in any order.

---

## Workflow

### Phase 1 — Diagnosis (load references/00-diagnosis.md)

Run Steps 1–9 progressively. Each step waits for the user's answer before
proceeding. Never present all steps at once.

**Steps 1–8**: Standard product diagnosis (problem, AI-native test, user AI
acceptance, data assets, domain complexity, team capability, constraints, timeline).

**Step 9**: Founding Team Asset Assessment — run this step when the team has
existing domain operations or technology. It surfaces non-replicable advantages:
  9A — Market position and customer assets
  9B — Supply chain and upstream relationships
  9C — Existing data assets (volume, quality, exclusivity)
  9D — Technical assets (models, code, research, industrial partnerships)
  9E — Team and execution capacity beyond the founders
  9F — Early validation signals and first customer hypothesis

After Step 9, combine the Product Brief (from Step 8) with the Founding Team
Asset Summary (from Step 9) into a single unified brief for user confirmation.

If a stakeholder synthesis from Mode A exists, use it to pre-fill answers where
possible and tell the user which steps you are skipping and why.

If a Delta Document from Mode C exists, use invalidated decisions as explicit
constraints: "上一版中 [X] 这个判断已被推翻，本次分析将从 [Y] 重新出发。"

---

### Phase 2 — Layer Analysis (user-selectable)

After confirming the Product Brief, present the four analysis layers:

  1. Business Layer    — strategy, business model, competitive moat
  2. Application Layer — product form, UX patterns, human-AI collaboration
  3. Technical Layer   — model selection, RAG/Agent/FT architecture, infra
  4. Data Layer        — data assets, ontology design, knowledge engineering

For each selected layer, load the reference file and conduct the analysis.
Where stakeholder research or a prior Delta Document exists, weave those inputs in
explicitly — cite which stakeholder or which prior decision is being referenced.

**After EACH layer**, always ask:
"需要为这一层生成执行级补充文档吗？面向开发或产品团队，可直接指导开工。"

Reference routing:
- Business layer         → references/01-business-layer.md
- Application layer      → references/02-application-layer.md
- Technical layer        → references/03-technical-layer.md
- Data layer             → references/04-data-layer.md
- Output templates       → references/05-output-templates.md
- Stakeholder research   → references/06-stakeholder-research.md
- Version comparison     → references/07-version-delta.md

---

### Phase 3 — Document Generation

Load references/05-output-templates.md and ask which deliverables to produce:
  [ ] Strategy Report (.md)
  [ ] Architecture Document (.md)
  [ ] Both

Name files with the current date: `strategy-report-YYYY-MM.md`.
This naming enables clean version comparison in future sessions.

Save and present all generated files.

---

### Phase 4 — PPT Generation

After the strategy report, offer to generate a PPT deck via the pptx-author skill.
Pass: full strategy report content, 14-slide outline from references/05-output-templates.md,
audience (investors and C-suite), key narrative (AI-native transformation thesis).

---

## Core Principle: The Transformation Test

Apply before producing any deliverable:

  "If you removed the AI entirely, would this product still exist in a degraded
   form — or would it simply not exist?"

- Still exists (degraded) → AI-enhanced. Strategy focuses on execution differentiation.
- Cannot exist → AI-native. Strategy leads with the transformation thesis.

Carry this distinction through every deliverable.

---

## Two-Level Output Model

**Strategic Level** (Phases 3-4): investors, board, CEO, CTO. "What and why."
2,500–4,000 words. Narrative prose with diagrams.

**Execution Level** (triggered in Phase 2): engineering leads, product managers.
"How." Specific schemas, prompts, user stories, flows. Separate files from the
strategy report.

**Stakeholder Research Level** (Mode A): raw inputs organized by stakeholder role.
Per-person records + synthesis. Feeds into Phase 1 and Phase 2 as context.

**Version Comparison Level** (Mode C): Decision Registry + Delta Document.
Tracks what changed, what was validated, what was invalidated. Feeds into the
next round of Phase 2 analysis.
