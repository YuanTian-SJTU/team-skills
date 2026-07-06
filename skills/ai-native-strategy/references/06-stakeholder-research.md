# Stakeholder Research Guide

## Purpose

Capture and organize inputs from different stakeholders before or during architecture
design. Each stakeholder type has a distinct perspective, vocabulary, and concern set.
Recording them separately — and synthesizing them explicitly — prevents the most common
AI product strategy failure: designing for the person in the room, not the full
stakeholder ecosystem.

This guide is used in two modes:

**Capture Mode**: Conduct a structured interview with a single stakeholder.
Generate a stakeholder document at the end.

**Synthesis Mode**: Given two or more existing stakeholder documents, produce a
Stakeholder Synthesis that surfaces alignment, tension, and gaps — to be read
before starting the layer-by-layer architecture analysis.

---

## Stakeholder Types and Interview Templates

### Type 1: CEO / 创始人

**Who they are**: Sets vision, owns the market thesis, makes final resource calls.
**What they care most about**: "Is this the right bet? Will it win?"

Interview focus areas:

```
1. VISION
   - What does the world look like in 3 years if this product succeeds?
   - What category are you creating or disrupting?

2. MARKET THESIS
   - Why is this the right moment? What changed in the last 12-24 months?
   - Who is the ideal first customer, and why do they need this now?
   - What does "winning" look like — market share, revenue, users, influence?

3. COMPETITIVE VIEW
   - Who are the real competitors (not the obvious ones)?
   - What is the one thing incumbents cannot do without cannibalizing themselves?
   - What is your unfair advantage?

4. INVESTMENT APPETITE
   - What is the budget envelope for the first 12 months (rough order of magnitude)?
   - What must be true at Month 6 to justify continued investment?
   - What would cause you to kill this product?

5. RISK TOLERANCE
   - What are the top 2-3 things that keep you up at night?
   - Is "move fast and break things" acceptable, or does this domain require caution?
```

Output document: `stakeholder-ceo-<name>.md`

---

### Type 2: 投资人 / VC

**Who they are**: Provides capital, expects returns, benchmarks against portfolio.
**What they care most about**: "Can this become a large, defensible business?"

Interview focus areas:

```
1. INVESTMENT THESIS
   - Why does this category deserve venture-scale investment?
   - What is the narrative in one sentence that makes LPs excited?
   - Which comparable exits or growth stories are you thinking of?

2. KEY METRICS
   - What are the 3-5 metrics you'll track in the first 18 months?
   - What does Series A readiness look like for this type of product?
   - What gross margin profile do you expect at scale?

3. MARKET SIZE
   - What is your TAM/SAM framing? Bottom-up or top-down?
   - What percentage of the market is realistically capturable in 5 years?

4. CONCERNS AND DUE DILIGENCE
   - What are the biggest risks you see that the founding team may be underweighting?
   - What questions do you want answered before the next check?
   - Who else are you watching in this space?

5. TIMELINE AND MILESTONES
   - What does the funding runway need to cover?
   - What are the non-negotiable milestones for the next round?
```

Output document: `stakeholder-investor-<name>.md`

---

### Type 3: CTO / 技术负责人

**Who they are**: Owns technical execution, team, and architecture decisions.
**What they care most about**: "Can we actually build this? With what team? At what risk?"

Interview focus areas:

```
1. CURRENT TECHNICAL LANDSCAPE
   - What is the existing tech stack (languages, frameworks, infra, data stores)?
   - What does the engineering team look like today (size, seniority, specializations)?
   - What are the biggest technical debts or constraints we are working around?

2. BUILD VS BUY PHILOSOPHY
   - What do you believe should be built internally vs. purchased or integrated?
   - What AI/ML capabilities does the team have today vs. need to hire or train?
   - Which foundation model providers are acceptable? Any that are off-limits?

3. INFRASTRUCTURE AND COMPLIANCE
   - Are there data residency or sovereignty requirements?
   - What latency SLAs are non-negotiable?
   - Are there existing security or compliance frameworks the product must fit into?

4. TEAM CAPACITY
   - How much engineering capacity can be dedicated to this in the first 6 months?
   - What is the hiring plan, and what roles are critical path?
   - What would overload the team and create quality/morale risk?

5. TECHNICAL RISKS
   - What parts of the proposed architecture concern you most?
   - Where do you see the highest probability of technical failure or delay?
   - What would you do differently from what's been proposed so far?
```

Output document: `stakeholder-cto-<name>.md`

---

### Type 4: CPO / 产品负责人

**Who they are**: Owns product vision, user research, and roadmap decisions.
**What they care most about**: "Will users love it? Does it solve the right problem?"

Interview focus areas:

```
1. USER UNDERSTANDING
   - Who is the primary user persona? Describe them in detail.
   - What does their current workflow look like (before this product)?
   - What is the single biggest frustration in how they work today?
   - Have you done user interviews? What surprised you most?

2. PRODUCT VISION
   - What does the ideal product experience feel like in 12 months?
   - What is the "first wow moment" — the interaction that makes users say
     "I've never seen anything like this"?
   - What would make users recommend this product to a colleague without being asked?

3. FEATURE PRIORITIES
   - What must be in v1 (non-negotiable)?
   - What should be in v1 but could be cut if needed?
   - What should be deferred to v2 no matter how many people ask for it?

4. COMPETITIVE PRODUCT LANDSCAPE
   - What existing products do target users compare this to?
   - What do those products do well that we must match?
   - What do they do poorly that we can exploit?

5. DESIGN PRINCIPLES
   - What are 2-3 product design principles you won't compromise on?
   - What is the right balance between AI autonomy and user control?
   - How much complexity is acceptable for the target user?
```

Output document: `stakeholder-cpo-<name>.md`

---

### Type 5: 域专家 / 行业顾问

**Who they are**: Deep domain knowledge; may be an advisor, consultant, or subject matter expert.
**What they care most about**: "Does this team understand the domain well enough?"

Interview focus areas:

```
1. DOMAIN KNOWLEDGE LANDSCAPE
   - What does it take to be considered expert in this domain?
   - What terminology, concepts, or frameworks are essential to know?
   - What do outsiders consistently get wrong about this domain?

2. DATA AND INFORMATION ECOSYSTEM
   - What data exists in this domain and who controls it?
   - What data is publicly available vs. proprietary vs. inaccessible?
   - What data standards or taxonomies exist that we should align with?

3. REGULATORY AND COMPLIANCE LANDSCAPE
   - What regulations apply? Which are most likely to affect product design?
   - Are there pending regulatory changes that could impact the product?
   - What do compliant companies in this domain do that others don't?

4. INCUMBENT AND COMPETITOR ANALYSIS
   - Who are the established players? What do they do well?
   - Where do existing solutions consistently fail domain users?
   - What would it take to displace an incumbent in a real enterprise account?

5. ADOPTION PATTERNS
   - How do domain professionals evaluate and adopt new tools?
   - Who are the internal champions typically — technical staff, management, end users?
   - What killed promising products in this space in the past?
```

Output document: `stakeholder-expert-<name>.md`

---

### Type 6: 种子用户 / 早期目标用户

**Who they are**: Real users who represent the core target persona; ideally already working
around the problem the product solves.
**What they care most about**: "Does this actually help me do my job better?"

Interview focus areas:

```
1. CURRENT WORKFLOW
   - Walk me through a typical day / week related to the problem this product addresses.
   - What tools do you use? In what order? Where do you switch between them?
   - Where do you spend the most time on tasks you consider low-value or frustrating?

2. PAIN POINTS AND WORKAROUNDS
   - What is the most painful thing about your current process?
   - Have you built any informal workarounds (spreadsheets, manual checklists, etc.)?
   - If you could eliminate one part of your job, what would it be?

3. DECISION-MAKING AND TRUST
   - When do you rely on tools vs. your own judgment?
   - How do you verify that a tool's output is correct?
   - Have you been burned by unreliable software before? What happened?

4. ADOPTION CONTEXT
   - Who else in your organization would need to use this product?
   - What would you need to see before recommending it to your manager?
   - What would make you stop using it after trying it?

5. WILLINGNESS AND ABILITY TO PAY
   - What tools do you currently pay for out of budget?
   - Who approves software purchases in your organization?
   - What price point would feel like an obvious yes? An obvious no?
```

Output document: `stakeholder-user-<name>.md`

---

## Capture Mode: How to Conduct an Interview

When the user indicates they want to record a stakeholder interview:

1. **Identify the stakeholder type** from context or ask directly:
   "这是哪类利益相关者？CEO / 投资人 / CTO / CPO / 域专家 / 种子用户？"

2. **Ask for the person's name or alias** (for document naming):
   "这位利益相关者怎么称呼？（用于文档命名，可以用代号）"

3. **Run the interview one section at a time** from the appropriate template above.
   Do not present all questions at once. Ask 1-2 questions, wait for response,
   summarize what you heard, then ask the next section.

4. **After all sections**, produce a structured document:

```
# 利益相关者调研 — [类型] [姓名/代号]
访谈日期：[日期]
产品：[产品名称]

## 关键洞察摘要
[3-5个最重要的洞察，bullet points]

## 详细记录

### [Section 1 title]
[Structured notes from this section]

### [Section 2 title]
...

## 未解决的问题
[Questions this interview raised that need follow-up or other stakeholder input]

## 对架构设计的影响
[How these inputs should specifically shape the Business / Application / Technical / Data layers]
```

Save as a file and present to the user.

---

## Synthesis Mode: Multi-Stakeholder Analysis

When two or more stakeholder documents exist and the user is about to begin architecture
design, generate a Stakeholder Synthesis document:

```
# 利益相关者综合分析
参与方：[list of stakeholders]
产品：[product name]

## 对齐点 (Alignment)
[Where all/most stakeholders agree — these are safe foundations for the architecture]

## 张力与冲突 (Tension)
[Where stakeholders disagree or have incompatible expectations]
[For each tension: describe the conflict, assess whose constraint is harder/softer,
 suggest how to resolve or trade off]

## 信息缺口 (Gaps)
[Critical questions that no stakeholder interview answered]
[Flag these as assumptions that need validation]

## 按架构层的综合建议

### 业务层影响
[Consolidated inputs that affect business model, go-to-market, competitive positioning]

### 应用层影响
[Consolidated inputs that affect UX design, interaction model, trust architecture]

### 技术层影响
[Consolidated inputs that affect model choice, infra, latency, compliance]

### 数据层影响
[Consolidated inputs that affect data strategy, ontology, privacy, flywheel design]

## 优先级建议
[Based on the full stakeholder picture, what should be prioritized in the first version
 and what should be deferred — and why]
```

This synthesis becomes the starting context for Phase 2 layer analysis.
