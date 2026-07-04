# Phase 1: Progressive Diagnosis Questionnaire

Run these 8 steps one at a time. Wait for the user's answer before continuing.
After Step 8, write a Product Brief and ask the user to confirm it.

---

## Step 1 — Product Core

Ask: "请描述你正在构建（或规划）的产品——它解决什么核心问题，目标用户是谁？"
     "Describe the product you're building or planning — what core problem does it solve,
      and who is the target user?"

Listen for:
- The problem domain (vertical: legal, medical, finance, education, etc.)
- Whether the problem is information-heavy, decision-heavy, or task-automation
- Who suffers from this problem (enterprise, consumer, developer)

---

## Step 2 — The AI-Native Test

Ask: "如果去掉 AI，这个产品还能存在吗（哪怕功能大打折扣）？还是说，没有 AI 它根本就不会存在？"
     "If you removed the AI entirely, would this product still exist in a degraded form —
      or would it simply not exist at all?"

Classify based on answer:
- "Still exists but worse" → AI-Enhanced track. Note this honestly; the strategy will
  focus on differentiation-through-execution rather than category creation.
- "Cannot exist at all" → AI-Native track. The transformation thesis is the lead.
- "Not sure" → Help them think through it: what is the core value delivery mechanism?
  Could a team of 1000 humans replicate it without AI? If yes, AI-enhanced.

---

## Step 3 — User Expectation & AI Acceptance

Ask: "你的目标用户对 AI 的接受程度如何？他们是技术敏感型用户，还是希望 AI ' 隐形' 在背后？"
     "How AI-savvy are your target users? Do they want to see and control the AI,
      or do they prefer AI to be invisible in the background?"

Listen for:
- Power users who want control → transparent AI, explain-ability matters
- Non-technical users who want results → invisible AI, trust through outcome quality
- Regulated industries → users need audit trails and human override

---

## Step 4 — Data Assets

Ask: "你们有哪些私有数据资产？请描述大概的量级、类型（文档、结构化数据、用户行为数据等）和质量。"
     "What private data assets do you have? Describe volume, type (documents, structured
      data, user behavioral data, etc.) and quality."

Listen for:
- Volume: KB / MB / GB / TB scale
- Structure: fully structured (DB), semi-structured (JSON/XML), unstructured (PDF/email)
- Quality: clean and labeled vs raw and noisy
- Exclusivity: is this data unique to you, or could competitors acquire similar data?

---

## Step 5 — Domain Knowledge Complexity

Ask: "你的业务领域有没有复杂的专业术语体系、概念层级关系，或者领域专家才懂的推理规则？"
     "Does your domain have complex terminology systems, concept hierarchies, or
      reasoning rules that only domain experts understand?"

Listen for:
- Yes, highly specialized → flag for ontology design in Data Layer
- Moderate → RAG with good chunking strategy may suffice
- No, general domain → standard retrieval approaches are fine

---

## Step 6 — Team Capability

Ask: "团队目前有 ML/AI 工程能力吗？能自研模型或做 fine-tuning，还是主要依赖 API 调用？"
     "Does your team have ML/AI engineering capability — can you fine-tune or train
      models, or are you primarily API-driven?"

Classify:
- Full ML capability → fine-tuning and custom models are on the table
- API-driven → RAG + prompt engineering + orchestration layer is the realistic path
- Hybrid → identify what's truly worth building vs buying

---

## Step 7 — Business Constraints

Ask: "有哪些硬性约束？比如：成本上限、响应延迟要求、数据合规（国内/境外）、行业监管。"
     "What are the hard constraints? Cost ceiling, latency requirements, data compliance
      (on-premise vs cloud), regulatory requirements."

Listen for:
- Cost: per-query cost ceiling that rules out certain models
- Latency: real-time (<1s) vs near-real-time (<5s) vs async (minutes OK)
- Data residency: must stay on-premise or in specific regions
- Regulation: healthcare (HIPAA), finance (SOC2), EU (GDPR), China (PIPL/MLSR)

---

## Step 8 — Timeline & Ambition

Ask: "你们希望多久上线第一个版本？以及 18 个月后，你们希望这个产品在市场上处于什么位置？"
     "How soon do you need the first version live? And 18 months from now, where do
      you want this product to be in the market?"

Listen for:
- Short timeline (<3 months) → must prioritize API-first, minimal custom infra
- Medium (3-9 months) → can invest in some custom components
- Long (>9 months) → full architecture design is warranted
- Market ambition: category leader vs niche champion vs acqui-hire target

---

## Product Brief Template

After Step 8, synthesize and present this to the user for confirmation:

---
**Product Brief — [Product Name or Working Title]**

**Classification:** AI-Native / AI-Enhanced

**Transformation Thesis (AI-Native only):**
[One sentence: what paradigm does this product break, and why now]

**Core Problem:** [2-3 sentences]

**Target User:** [Who, their context, their current pain]

**Data Assets:** [Summary of what they have and its strategic value]

**Key Constraints:** [Top 3 constraints that will shape architecture]

**Layer Priorities:** [Which of the 4 layers need deepest analysis, based on answers]

**Timeline:** [First version target + 18-month ambition]
---

Ask: "这份产品摘要准确吗？有需要补充或修正的地方吗？"
     "Does this Product Brief look accurate? Anything to add or correct?"

Proceed to Phase 2 only after user confirms.
