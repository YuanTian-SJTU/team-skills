---
name: ai-native-strategy
description: |
  Use this skill whenever a user wants to design, plan, analyze, or evaluate the technical
  strategy and architecture of an AI-native product. Trigger on any of the following:
  mentions of "AI原生产品", "AI产品架构", "AI技术战略", "AI战略规划", "模型选型",
  "RAG架构", "Agent架构", "知识图谱", "AI产品设计", "数据飞轮", "AI战略报告";
  or requests to design an AI-first product from scratch; or evaluate technology choices
  for an AI product; or produce a strategy report / architecture document / pitch deck
  for an AI product for investors or executives. Also trigger when the user wants to
  record or capture stakeholder research inputs — such as interviews with CEO, investors,
  CTO, CPO, domain experts, or early users — before or during architecture design.
  This skill is especially valuable when the user wants to articulate WHY their product
  is transformatively AI-native rather than just AI-enhanced.
---

# AI-Native Product Technical Strategy & Architecture

## Purpose

Guide the user through a structured dialogue to design the technical strategy and
architecture of an AI-native product, then generate deliverables at two levels:

**Strategic deliverables** (for investors and C-suite):
- Strategy Report (.md, convertible to .docx)
- Architecture Document (.md with Mermaid diagrams)
- PPT Deck (.pptx via pptx-author skill)

**Execution-level supplements** (for development and product teams, on request):
- Technical Layer → Data Schema Draft + Orient Prompt Template + ERP Integration Checklist
- Application Layer → User Stories + Main User Flow + Notification Specification

**Stakeholder research documents** (captured before or during architecture design):
- Per-stakeholder interview records (CEO, investor, CTO, CPO, domain expert, seed user)
- Multi-stakeholder synthesis (alignment, tensions, gaps, layer-by-layer implications)

The central narrative thread throughout all work: **AI-native ≠ AI-enhanced.**
An AI-native product is one that would be impossible — not merely worse — without AI.
This distinction is what makes it transformative, and it must be visible in every
deliverable, especially those aimed at investors and executives.

---

## Language Rule

Detect the user's language from their first message. Respond and produce all outputs
in that language (Chinese or English). If the user switches language mid-conversation,
follow their lead. All internal instructions in this skill are in English and should
not appear verbatim in any user-facing output.

---

## Mode Detection

At the start of each session, determine which mode the user is in:

**Mode A — Stakeholder Research**
Triggered when the user mentions: recording an interview, capturing inputs from a
specific stakeholder role (CEO, investor, CTO, CPO, domain expert, early user),
or says something like "记录CEO的想法", "投资人反馈", "访谈记录", "用户调研".
→ Load references/06-stakeholder-research.md and enter Capture Mode.
→ After each interview, offer: "要生成利益相关者综合分析吗？"

**Mode B — Architecture Design**
Triggered when the user wants to design, plan, or analyze the AI product strategy.
→ Run Phases 1–4 below.
→ Before starting Phase 1, check if stakeholder research documents exist in this
  session or if the user mentions having done stakeholder research. If yes, offer
  to run Synthesis Mode first: "检测到已有利益相关者调研记录，是否先生成综合分析，
  作为架构设计的输入？"

Both modes can run in the same session. Stakeholder research can happen before,
during, or after architecture design.

---

## Workflow

### Phase 0 — Stakeholder Research (Mode A, load references/06-stakeholder-research.md)

**Capture Mode**: Interview one stakeholder at a time using the template for their type.
Run sections one at a time — never present all questions at once. After each section,
summarize what you heard before moving to the next. At the end, produce a structured
stakeholder document and save it as a file.

**Synthesis Mode**: When two or more stakeholder documents exist, produce a
multi-stakeholder synthesis that surfaces alignment, tensions, and gaps across all
inputs, organized by architecture layer. This synthesis becomes the starting context
for Phase 2.

Stakeholder types supported: CEO/创始人, 投资人/VC, CTO/技术负责人, CPO/产品负责人,
域专家/行业顾问, 种子用户/早期目标用户.

---

### Phase 1 — Diagnosis (load references/00-diagnosis.md)

Run the 8-step progressive dialogue. Each step waits for the user's answer before
proceeding to the next. Do NOT present all questions at once.

If a stakeholder synthesis exists from Phase 0, use it to pre-fill answers where
possible and skip questions the synthesis already answered. Tell the user which
questions you're skipping and why.

After Step 8, synthesize a Product Brief (1-2 paragraphs) and show it to the
user for confirmation before proceeding.

---

### Phase 2 — Layer Analysis (user-selectable)

After confirming the Product Brief, present the four analysis layers and ask the user
which to prioritize or skip:

  1. Business Layer    — strategy, business model, competitive moat
  2. Application Layer — product form, UX patterns, human-AI collaboration
  3. Technical Layer   — model selection, RAG/Agent/FT architecture, infra
  4. Data Layer        — data assets, ontology design, knowledge engineering

For each selected layer, load the corresponding reference file and conduct the
analysis. Output per layer: key decisions + recommended approach + risk flags.
Let the user steer depth — they can ask to go deeper on any sub-topic.

Where stakeholder research documents exist, weave their inputs into the analysis
explicitly — cite which stakeholder raised which concern or constraint.

**After completing EACH layer analysis, always ask:**
"需要为这一层生成执行级补充文档吗？这类文档面向开发团队或产品团队，
 粒度比战略分析更细，可以直接指导开工。"

If the user says yes, load the corresponding reference and generate the
execution-level supplement before moving to the next layer.

Reference routing:
- Business layer    → load references/01-business-layer.md
- Application layer → load references/02-application-layer.md
- Technical layer   → load references/03-technical-layer.md
- Data layer        → load references/04-data-layer.md
- Output format     → load references/05-output-templates.md
- Stakeholder research → load references/06-stakeholder-research.md

---

### Phase 3 — Document Generation

After layer analysis, load references/05-output-templates.md and ask the user
which deliverables they want:
  [ ] Strategy Report (.md)
  [ ] Architecture Document (.md)
  [ ] Both

Generate the selected documents following the templates exactly.
Save files to the working directory and present them to the user.

---

### Phase 4 — PPT Generation

After the strategy report is complete, offer to generate a PPT deck.
If the user agrees, invoke the pptx-author skill and pass:
- The full strategy report content
- Instruction to follow the 14-slide outline in references/05-output-templates.md
- Audience: investors and C-suite executives
- Key narrative: transformative AI-native distinction

---

## Core Principle: The Transformation Test

Before producing any deliverable, apply this test to the product being analyzed.
The answer shapes the entire narrative:

  "If you removed the AI entirely, would this product still exist in a degraded
   form — or would it simply not exist?"

- Still exists (degraded) → AI-enhanced product. The strategy should honestly
  acknowledge this and focus on competitive differentiation through AI execution quality.
- Simply cannot exist → AI-native product. The strategy should lead with the
  transformation thesis: what paradigm does this break, and why now.

Surface this distinction explicitly in the Business Layer analysis and carry it
through to all deliverables.

---

## Two-Level Output Model

This skill produces outputs at two distinct granularity levels. Understand the
difference before generating anything:

**Strategic Level** (Phases 3-4):
- Audience: investors, board, CEO, CTO
- Granularity: "what and why" — architecture decisions, competitive positioning,
  business model logic, risk framing
- Format: narrative prose with diagrams; 2,500-4,000 words

**Execution Level** (triggered during Phase 2, on request):
- Audience: engineering leads, product managers, developers
- Granularity: "how" — specific schemas, prompt templates, user stories,
  interaction flows, notification specs
- Format: structured specifications that teams can act on directly
- These are separate files from the strategy report, not included in it

**Stakeholder Research Level** (Phase 0, Mode A):
- Audience: architecture design sessions; the person building the strategy
- Granularity: "who thinks what and why" — raw inputs organized by stakeholder
- Format: per-person interview records + multi-stakeholder synthesis
- These feed into Phase 1 and Phase 2 as input context, not as deliverables themselves
