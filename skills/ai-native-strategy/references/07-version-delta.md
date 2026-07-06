# Version Comparison Guide

## Purpose

Enable structured comparison between two versions of an AI product strategy analysis.
As AI capabilities evolve rapidly and market conditions shift, the decisions made in
one analysis session may need to be revisited. This guide defines how to extract
prior decisions, re-evaluate them, and produce a Delta Document that makes visible
what changed and why.

---

## How Version Comparison Works

Claude has no memory between sessions. "Version comparison" is therefore explicit:
the user provides the previous strategy report as an uploaded file, and this guide
instructs Claude how to process it.

**Trigger**: User uploads a previous strategy/architecture document AND says something
like "做第二版分析", "对比上一版", "update last analysis", "what changed since v1".

**Do not enter comparison mode** if the user uploads a document without indicating
they want a comparison — they may just want to reference it.

---

## Step 1: Extract the Decision Registry from the Prior Document

Read the uploaded prior document and extract a structured **Decision Registry** —
the set of key decisions and hypotheses that were made. Do not summarize prose;
extract specific, testable claims.

For each decision found, record:

```
Decision ID: [D-01, D-02, ...]
Layer: [Business / Application / Technical / Data / Network]
Decision: [The specific choice made — e.g., "Use RAG over fine-tuning for the Orient layer"]
Rationale given: [Why this decision was made at the time]
Assumptions: [What had to be true for this decision to be correct]
Confidence at time: [High / Medium / Low — infer from language in document]
```

Typical decisions to look for:
- Business: monetization model, primary moat, target customer segment
- Application: product archetype, interaction mode, trust architecture
- Technical: model selection, RAG/FT/PE choice, agent pattern, infra choice
- Data: ontology level, RAG pattern, flywheel design
- Network (if applicable): network topology, cold start strategy, platform governance

Present the Decision Registry to the user and ask:
"以上是上一版分析中提取的关键决策，共 [N] 项。确认后我们开始逐项评估哪些仍然成立，哪些需要更新。"

---

## Step 2: Identify What Changed

Before re-analyzing each decision, ask the user what has changed since the last version.
Run these questions one at a time:

**Change 1 — AI Capability Shifts**
Ask: "自上次分析以来，有没有出现新的模型或AI能力，改变了你们的技术选型判断？
     例如：新的推理模型、更强的中文能力、更低的推理成本、新的 agent 框架。"

**Change 2 — Market / Customer Feedback**
Ask: "自上次分析以来，有没有从客户、合作方或市场收到任何反馈？
     有没有做过POC、用户访谈、或者早期销售尝试？结果如何？"

**Change 3 — Competitive Landscape**
Ask: "有没有出现新的竞争者，或者现有竞争者有明显的动作？"

**Change 4 — Internal Changes**
Ask: "团队、资源、时间线、或者产品范围有没有变化？
     比如：融到钱了、关键成员加入或离开、决定先聚焦某个子市场。"

**Change 5 — Stakeholder Input**
Ask: "这一轮有没有新的利益相关者调研记录可以参考？
     如果有，请上传或告诉我关键内容。"

Record all changes as a **Change Log** that will appear in the Delta Document.

---

## Step 3: Re-evaluate Each Decision

For each decision in the Decision Registry, evaluate its current status:

**✅ Validated** — The decision holds. New evidence or experience supports it.
State: what confirmed it, and whether confidence increased or stayed the same.

**❌ Invalidated** — The decision was wrong or is no longer applicable.
State: what changed, why the original assumption failed, what the new decision is.

**🔄 Updated** — The direction is right but specifics need revision.
State: what the original was, what it becomes, and why.

**⏳ Still Open** — The decision depends on something not yet known.
State: what information would resolve it and how to get it.

**🆕 New Decision** — A new decision point emerged that didn't exist in v1.
State: the new decision and the rationale.

---

## Step 4: Produce the Delta Document

Generate a Delta Document as a separate file from the v2 strategy report.

```
# Strategy Delta: [v_previous] → [v_current]
生成日期：[date]
产品：[product name]
上一版日期：[date of previous analysis]

---

## 变更背景 (What Changed)

### AI能力变化
[Changes to foundation models, APIs, costs, new frameworks]

### 市场与客户反馈
[Validation or invalidation signals from the real world]

### 竞争格局变化
[New entrants, incumbent moves, pricing changes]

### 内部变化
[Team, funding, scope, timeline]

---

## 决策评估 (Decision Evaluation)

### ✅ 已验证的决策 (N items)
[List decisions with evidence that confirmed them]

### ❌ 已推翻的决策 (N items)
[List decisions with explanation of what failed and what replaces them]

### 🔄 已更新的决策 (N items)
[List decisions with before → after and rationale]

### ⏳ 仍待验证的决策 (N items)
[List unresolved decisions with what's needed to resolve them]

### 🆕 新增决策点 (N items)
[New decisions that didn't exist in the previous version]

---

## 核心变化摘要 (Executive Summary of Changes)
[3-5 sentences: what is fundamentally different between v1 and v2,
 and what it means for the product direction]

---

## 对下一版的影响 (Implications for v_next)
[What to prioritize in the next iteration given what was learned]
[What hypotheses to test before v3]
```

---

## Version Naming Convention

Recommend the user name versions by date, not by number, to make the timeline clear:

```
strategy-report-2026-07.md       ← first analysis
strategy-report-2026-10.md       ← second analysis
delta-2026-07-to-2026-10.md      ← delta between them
```

If storing on GitHub (recommended for team access):
```
analysis/
├── 2026-07/
│   ├── strategy-report.md
│   ├── architecture-doc.md
│   └── stakeholder-synthesis.md    ← if applicable
├── 2026-10/
│   ├── strategy-report.md
│   ├── delta-from-2026-07.md
│   └── ...
```

---

## What Makes a Good Version Cadence

**Trigger a new version when any of the following occur:**
- A foundation model with significantly different capability/cost is released
- First real customer feedback is received (positive or negative)
- A direct competitor launches or raises funding
- The team makes a significant scope or strategy pivot
- 6 months have passed since the last version (regardless of changes)

**Do NOT trigger a new version for:**
- Minor product feature additions
- Routine operational decisions
- Changes that don't affect the four-layer architecture

The value of version discipline is the **Decision Registry** — having an auditable
record of what you believed, when, and whether it turned out to be right. This is
how fast-moving teams avoid re-litigating decisions and how investors track the
team's judgment quality over time.
