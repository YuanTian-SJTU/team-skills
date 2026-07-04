# Business Layer Analysis Guide

## Purpose
Help the user articulate the business strategy of their AI-native product in terms
that resonate with investors and C-suite executives. The central goal is to make
the transformative nature of the product legible — not as a feature list, but as
a paradigm shift with durable competitive advantages.

---

## 1. The Transformation Thesis

This is the most important output of the business layer. It answers three questions
that investors and executives actually care about:

**Q1 — What paradigm does this break?**
Not "what problem does it solve" but "what existing mental model becomes obsolete."
Good examples:
- "Search assumed humans filter results. We assume AI synthesizes answers."
- "SaaS assumed humans do the work. We assume AI does the work, humans supervise."
- "Advisory assumed scarce expert time. We make expert reasoning infinitely scalable."

**Q2 — Why is now the inflection point?**
The technology has existed in some form before. What changed in the last 12-24 months
that makes this viable today? Push the user to be specific:
- Foundation model capability crossing a threshold (e.g., GPT-4-level reasoning)
- Data infrastructure becoming commodity (vector DBs, embedding APIs)
- User behavior shift (ChatGPT normalized AI interaction for the mass market)
- Regulatory window opening or closing

**Q3 — Why can't incumbents simply add this feature?**
The best AI-native products exploit an "adaptation trap" — incumbents are structurally
unable to adopt the new paradigm without cannibalizing their existing business.
Help the user identify this specifically for their domain.

---

## 2. AI-Native vs AI-Enhanced Classification

Use this framework to anchor the strategy:

| Dimension | AI-Native | AI-Enhanced |
|-----------|-----------|-------------|
| Core value delivery | AI is the mechanism | AI improves an existing mechanism |
| Without AI | Product does not exist | Product exists but is slower/worse |
| Business model | Structured around AI cost curves | Layered onto existing pricing |
| Moat | Data flywheel + model improvement | Feature advantage (erodable) |
| Narrative | Category creation | Category leadership |

If the product is AI-Enhanced, the strategy must honestly position it as category
leadership, not category creation. Trying to claim transformation for an enhanced
product will undermine credibility with sophisticated investors.

---

## 3. Competitive Moat Framework

For AI products, moats come from three sources. Help the user identify which apply:

**Moat 1: Data Flywheel**
- More users → more interaction data → better model → better product → more users
- Key question: does user interaction data actually improve model quality in your product?
- If yes: quantify the feedback loop latency and the quality delta per data doubling
- Strongest moat; takes 12-24 months to become defensible

**Moat 2: Domain Data Exclusivity**
- You have access to data that competitors cannot get (proprietary, licensed, or generated)
- Key question: is this data truly exclusive or just a head start?
- Head starts erode; true exclusivity (contractual, structural) compounds

**Moat 3: Workflow Lock-in**
- AI becomes embedded in the user's daily workflow; switching costs are behavioral
- Key question: how many decisions per day does the AI touch for the user?
- High-frequency touch points create muscle memory and institutional knowledge lock-in

Present these three options to the user and help them rank which applies most strongly.
A convincing investor narrative leads with the strongest moat and explains why it compounds.

---

## 4. Business Model Analysis for AI Products

AI-native products face unique cost structure challenges. Walk through these with the user:

**Inference Cost Structure**
- Per-query cost is a new line item that traditional SaaS didn't have
- Rule of thumb: target <10% of revenue on inference costs at scale
- If current cost per query is high, what is the path to reduce it?
  (model distillation, caching, prompt optimization, smaller specialized models)

**Monetization Model Options**

| Model | Works When | Risk |
|-------|-----------|------|
| Usage-based (per query/token) | Clear per-use value | Revenue volatility |
| Seat-based SaaS | AI is a productivity tool per person | Doesn't capture value of high-usage users |
| Outcome-based | Measurable ROI per use (e.g., cost saved) | Hard to instrument |
| Platform/Marketplace | AI enables a two-sided market | High complexity |

Help the user identify which model aligns with their transformation thesis and
user behavior. The business model should feel like a natural extension of how
the product creates value — not retrofitted.

**Unit Economics Pressure Points**
- LTV/CAC: AI often enables lower CAC (virality, word-of-mouth from "wow moments")
  but must be analyzed against higher COGS from inference
- Gross margin target: AI-native SaaS should target 60-70%+ at scale
  (below this, the model may be structurally challenged)

---

## 5. Risk Matrix for Investors

Proactively surface these risks and show mitigation strategies.
Sophisticated investors will ask about them — it's better to lead with them.

| Risk | Mitigation |
|------|-----------|
| Foundation model dependency | Multi-model strategy; abstraction layer over providers |
| Model commoditization | Moat from data/workflow, not model capability itself |
| Regulatory / compliance | Design for compliance-first; audit trails built in |
| Data privacy | On-premise option; data isolation architecture |
| Hallucination / reliability | Evals infrastructure; human-in-the-loop for high-stakes decisions |
| Talent | ML platform strategy over individual ML hires |

---

## Output for Business Layer

Produce a structured summary with these sections:
1. Transformation Thesis (3-4 sentences)
2. AI-Native Classification + justification
3. Primary Competitive Moat + compounding mechanism
4. Business Model recommendation + unit economics sketch
5. Top 3 risks + mitigations

This becomes the core of Section 2-4 of the Strategy Report.
