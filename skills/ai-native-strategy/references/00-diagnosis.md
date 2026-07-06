# Phase 1: Progressive Diagnosis Questionnaire

## Step 0 — Project Identification

Ask this before anything else, every session:

"这个分析属于哪个项目？请给这个项目起一个简短的名字（中文或英文都可以，我会自动转成标准格式）。
 如果是新项目，给个名字；如果是已有项目的更新版分析，告诉我项目名。"

From the user's answer, derive a **Project ID**:
- Convert to lowercase kebab-case English
- Max 30 characters
- Remove special characters
- Examples: "智慧供应链决策系统" → `smart-supply-chain`, "医疗AI平台" → `medical-ai-platform`

Show the derived ID to the user for confirmation:
"项目ID：`<project-id>`，所有文件将存放在 `analysis/<project-id>/` 下。确认吗？"

Store `{project_id}` and `{analysis_date}` (current YYYY-MM) as session variables.
Reference these in every file name and GitHub path generated in this session.

If the user says this is a version update of an existing project, note the previous
version date so Mode C (version comparison) can reference it.

---


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

---

## Step 9 — Founding Team Asset Assessment
*(Only run this step when the product is being built by a founding team with existing
 domain operations or technology — i.e., this is not a first-time researcher building
 a prototype. Skip if the user is designing a hypothetical product.)*

This step surfaces the team's non-replicable starting advantages. The goal is not
to list credentials but to identify what competitors would need 3-5 years to replicate.
Run sub-questions one at a time. Probe for specifics — vague answers ("we have good
relationships") are not useful. Ask: "Can you give me a concrete example?"

**Sub-step 9A — Market Position & Customer Assets**

Ask: "目前有多少活跃客户/合作方？能描述一下最核心的3-5家吗——规模、合作年限、你们在他们采购中的占比？"
     "How many active customers/partners do you have? Describe the top 3-5 —
      their size, years of relationship, and your share of their procurement."

Listen for:
- Customer concentration risk (top 1 customer = >40% of revenue is a flag)
- Depth of relationships (can they call the CEO directly? Do they have exclusivity?)
- Whether customers would be the first users of the AI product

**Sub-step 9B — Supply Chain & Upstream Relationships**

Ask: "上游（钢厂/一级代理/物流/金融机构）有哪些直接合作关系？有没有独家或优先协议？"
     "What direct relationships do you have upstream (mills, tier-1 agents, logistics,
      financial institutions)? Any exclusive or preferred arrangements?"

Listen for:
- Direct mill relationships (vs. buying through other distributors)
- Logistics network coverage (own fleet vs. partnerships)
- Supply chain finance access (who extends credit, on what terms)
- Information advantages (early access to pricing, capacity, policy changes)

**Sub-step 9C — Data Assets**

Ask: "现有系统里有哪些历史数据？大概的时间跨度、交易量级、字段完整度怎么样？有没有已经结构化的数据，还是主要在 Excel 或 ERP 里？"
     "What historical data exists in your current systems? Rough time span, transaction
      volume, field completeness? Is it structured in a DB or mainly in Excel/ERP?"

Listen for:
- Transaction history: years of data, number of transactions, SKU coverage
- Pricing data: historical price points, negotiation records, contract terms
- Demand data: order patterns, lead times, cancellation rates
- Quality: clean and consistent vs. fragmented across systems
- Exclusivity: is this data unique to you, or would any distributor have similar data?

**Sub-step 9D — Technical Assets**

Ask: "技术侧目前有哪些积累？包括已有的模型、代码库、已发表或在研的成果、与工业企业合作的项目经验。"
     "What technical assets exist today? Models, codebases, published or ongoing
      research, and any joint projects with industrial enterprises."

Listen for:
- Domain-specific models (fine-tuned on industrial data vs. general purpose)
- Existing knowledge bases or ontologies in the target domain
- Validated technical results (published evals, production deployments, POCs)
- Relationships with industrial partners that provide data or deployment access

**Sub-step 9E — Team & Execution Capacity**

Ask: "除了两位创始人，现在还有哪些核心人员？商业侧和技术侧各自的执行能力怎么评估？"
     "Beyond the two founders, who else is on the team? How would you assess execution
      capacity on the business side and technical side respectively?"

Listen for:
- Business team: salespeople, operations, customer success
- Technical team: engineers, ML researchers, data engineers
- Gaps: what critical capability is missing today
- Bandwidth: can the current team run existing business AND build the new product?

**Sub-step 9F — Early Validation**

Ask: "到目前为止，有没有任何概念验证？哪怕是非正式的：客户表达了兴趣、用户愿意试用、某个功能有人愿意付钱。第一个最可能买单的客户是谁？"
     "Has any form of validation happened yet — even informal? A customer expressing
      interest, a user willing to pilot, someone willing to pay for a feature.
      Who is most likely to be the first paying customer?"

Listen for:
- Letters of intent, pilot agreements, paid POCs
- Specific named potential customers (vs. vague "many customers are interested")
- Willingness-to-pay signal: what price point, what value proposition
- Who is the internal champion at the first customer

---

## Founding Team Asset Brief Template

After Step 9, produce a structured summary:

---
**创始团队资产摘要**

**核心市场地位：** [客户数量、关键客户描述、市场覆盖范围]

**供应链资产：** [上游关系、物流覆盖、金融资源、信息优势]

**数据资产：** [交易数据规模/时间跨度/完整度、独特性评估]

**技术资产：** [已有模型/代码/研究成果、工业部署经验]

**团队现状：** [商业侧执行力、技术侧执行力、关键缺口]

**最快路径到第一个付费客户：** [具体客户、关系基础、价值主张]

**不可复制的核心优势：** [竞争对手需要几年才能匹配的1-2项资产]
---

Fold this into the Product Brief from Step 8 and present the combined brief for
user confirmation before proceeding.
