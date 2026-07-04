# Technical Layer Analysis Guide

## Purpose
Define the technical architecture that implements the AI-native product strategy.
This guide is written for technical users (engineers, CTOs, architects) who need
to make specific technology decisions, not just high-level choices.

---

## 1. Model Selection Matrix

Evaluate models across four dimensions. Build a comparison table for the user's
specific use case.

**Dimension 1: Capability**
- Reasoning depth: does the task require multi-step logical inference?
- Context window: what is the maximum input length needed?
- Modality: text-only vs multimodal (image, audio, structured data)
- Language: primarily Chinese, English, or multilingual?
- Domain knowledge: does the model need deep domain knowledge baked in,
  or will RAG supply it?

**Dimension 2: Cost**
- Input/output token cost at current volume
- Projected cost at 10x and 100x scale
- Fine-tuning cost if applicable
- Total cost of ownership including infra

**Dimension 3: Latency**
- Time-to-first-token (TTFT) for streaming UX
- Total generation time for batch workflows
- P99 latency under load

**Dimension 4: Compliance**
- Data residency: which regions are acceptable?
- Is the model API provider compliant with relevant regulations (PIPL, GDPR, HIPAA)?
- On-premise deployment: is it possible if required?
- Model transparency: is the model open-weight or black-box?

**Model Strategy Patterns**

| Pattern | When to Use |
|---------|------------|
| Single frontier model | Prototyping; high-stakes tasks where quality >> cost |
| Router + specialized models | Different tasks need different capabilities; cost optimization at scale |
| Cascade (small → large) | Most queries resolved by small model; hard ones escalated to large |
| Open-weight self-hosted | Data residency requirements; cost control at scale; fine-tuning needed |
| Fine-tuned domain model | Proprietary domain knowledge; latency requirements; cost optimization |

---

## 2. The Core Architecture Decision: RAG vs Fine-Tuning vs Prompt Engineering

This is the most frequently misunderstood decision in AI product architecture.
Help the user think through it clearly.

**Decision Framework**

Ask these questions in order:

Q1: Is the required knowledge already in the foundation model?
- Yes → Prompt engineering may be sufficient. Test before building.
- No → Need RAG or fine-tuning.

Q2: Is the knowledge dynamic (changes frequently) or static?
- Dynamic (updated daily/weekly) → RAG. Fine-tuning cannot be updated continuously.
- Static or slow-changing → Fine-tuning or RAG both viable.

Q3: Is the task about knowledge retrieval or behavioral adaptation?
- Knowledge retrieval ("answer questions about our docs") → RAG
- Behavioral adaptation ("respond in our tone", "follow our output format") → Fine-tuning
- Both → RAG + fine-tuning (uncommon; high cost/complexity)

Q4: What is the acceptable latency?
- <1s → RAG with optimized retrieval; fine-tuned small model
- 1-5s → Full RAG pipeline viable
- >5s → Async workflows; larger models acceptable

**Hybrid Architecture (most production systems)**
Reality: most production AI products use Prompt Engineering as the baseline,
add RAG for knowledge grounding, and consider fine-tuning only for specific
high-value behavioral patterns. Start with the simplest stack that works.

---

## 3. RAG Architecture Decisions

If RAG is part of the architecture, these are the key design decisions:

**Chunking Strategy**
- Fixed-size chunks: simple, works for homogeneous content
- Semantic chunks: split on meaning boundaries; better for heterogeneous content
- Hierarchical chunks: parent document + child chunks; enables context expansion
- Rule: chunk size should match the granularity of the user's typical query

**Embedding Model Selection**
- General: text-embedding-3-large (OpenAI) or BGE (BAAI, open-weight, strong Chinese support)
- Domain-specific: consider fine-tuning embeddings if retrieval quality is poor
- Multilingual: BGE-M3 or multilingual-e5 if Chinese + English needed

**Retrieval Strategy**
- Dense retrieval (vector similarity): good for semantic queries
- Sparse retrieval (BM25): good for keyword/entity queries
- Hybrid (dense + sparse + reranking): best recall; recommended for production
- Graph RAG: add when ontology/knowledge graph is in use (see Data Layer)

**Reranking**
Always add a reranking step between retrieval and generation for production systems.
Cross-encoder rerankers (BGE-reranker, Cohere Rerank) significantly improve
precision at minimal additional latency cost.

---

## 4. Agent Architecture Patterns

If the product involves autonomous multi-step task execution, select an agent pattern:

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| ReAct | Reason + Act loop; single agent with tools | Simple task automation with well-defined tool set |
| Plan-and-Execute | Planner generates steps; executor runs them | Complex tasks needing upfront decomposition |
| Multi-Agent | Specialized agents collaborate via message passing | Tasks requiring parallel execution or deep specialization |
| Supervisor + Workers | Orchestrator delegates to subagents | Workflows with clear task decomposition and quality control |

**Agent Design Principles**
1. Make each agent's scope as narrow as possible — narrow agents fail more predictably
2. Design failure modes explicitly: what does the agent do when it's uncertain?
3. Every agent action that has side effects must be logged for audit and replay
4. Human checkpoints: identify which steps require human approval before proceeding

---

## 5. Inference Infrastructure

**Self-hosted vs API trade-off**

| Factor | Use API | Self-host |
|--------|---------|-----------|
| Development phase | Always | Never |
| Data residency | If provider is compliant | If required by regulation |
| Cost at scale | Until inference cost >15% of revenue | After this threshold |
| Latency SLA | If provider meets SLA | If <100ms P99 required |
| Model customization | If standard models suffice | If fine-tuned model needed |

**Inference Optimization Stack (self-hosted)**
- Serving: vLLM (best throughput), TGI (HuggingFace), Ollama (local dev)
- Quantization: AWQ or GPTQ for 2-4x memory reduction with <5% quality loss
- Batching: continuous batching is critical for throughput under concurrent load
- Caching: semantic caching (e.g., GPTCache) for high-repetition query patterns

---

## 6. Observability & Evals Architecture

An AI product without an evals infrastructure is flying blind.
This is the engineering investment that enables the data flywheel.

**Minimum Viable Evals Stack**
1. Logging: every LLM call logged (input, output, latency, cost, model version)
2. Online evals: lightweight automated checks on live traffic
   - Format validation (did the output match expected schema?)
   - Safety checks (did the output violate content policies?)
   - Business metric proxies (did the user complete their task?)
3. Offline evals: a golden dataset of input/expected-output pairs
   - Expand this dataset as you discover failure modes
   - Run before every model/prompt change

**LLM-as-Judge**
For tasks where ground truth is ambiguous (writing quality, reasoning quality),
use a stronger LLM to evaluate outputs. This scales where human evaluation doesn't.
Key: build a calibration set where you know human and LLM judgment agree.

---

## Output for Technical Layer

Produce a structured summary:
1. Model strategy: selected approach + reasoning (cost/capability/compliance table)
2. Core architecture: RAG / FT / PE decision + justification
3. RAG design decisions (if applicable): chunking, retrieval, reranking choices
4. Agent pattern (if applicable): selected pattern + human checkpoint design
5. Inference infrastructure: API vs self-hosted decision + optimization path
6. Evals plan: minimum viable evals stack for Day 1

---

## Execution-Level Supplement (generate when user requests after Technical Layer analysis)

This section is for teams that need to move from architectural decisions to actual
implementation. Generate three documents as separate files when requested.

---

### Supplement A: Core Data Schema Draft

Generate a schema specification covering the main entities identified in the
Technical Layer analysis. For each entity, produce:

```
Entity: [EntityName]
Storage: [Graph DB node / Relational table / Document store]
Fields:
  - field_name: type | constraints | description
  - ...
Indexes: [which fields to index and why]
Relationships: [edges to other entities with cardinality]
```

Focus on the entities that are directly needed for the OODA loop to function in
the first version. Mark fields as [MVP] or [Phase 2] to help teams prioritize.
Include a note on which fields feed the data flywheel (i.e., are written by user
interactions and read by model improvement pipelines).

---

### Supplement B: Orient Prompt Template

The Orient prompt is the most critical engineering artifact in an AI-native product
using this architecture. Generate a versioned prompt template:

```
## Orient Prompt Template v1.0

### System Instruction
[Define the AI's role, expertise, and output constraints.
 Include: domain context, what the AI knows, what it does NOT know,
 and the exact JSON output format it must produce.]

### Input Variables
{signal}: [description, format, example]
{graph_context}: [description, format, example — entities and relationships
                  retrieved from knowledge graph]
{rag_results}: [description, format, example — retrieved document chunks]
{company_context}: [description, format — company-specific constraints
                    like risk tolerance, key customers, current inventory state]

### Prompt Body
[The actual prompt text with {variable} placeholders.
 Include chain-of-thought instructions: ask the model to reason step by step
 before producing the final JSON.
 Include explicit instructions for expressing uncertainty.]

### Expected Output Schema
{
  "interpretation": "string — 1-2 sentences",
  "confidence": "float 0.0-1.0",
  "impact_assessment": [
    {"entity": "string", "risk_level": "high|medium|low", "reason": "string"}
  ],
  "recommended_actions": [
    {"action": "string", "rationale": "string", "urgency": "string", "priority": 1}
  ],
  "reasoning_chain": "string — internal reasoning summary",
  "data_gaps": ["string — what information would improve this assessment"]
}

### Failure Modes to Avoid
- [List 3-5 known failure patterns and how the prompt guards against them]

### Evaluation Criteria
- [What does a good Orient output look like? Use these for evals golden dataset]
```

After generating the template, note:
- Which parts are fixed vs. which parts should be iterated based on flywheel signals
- What the minimum "golden dataset" for evals should look like (5-10 examples)
- How to version and change-manage prompt updates

---

### Supplement C: ERP Integration Checklist

For the Observe layer to function, the system needs structured data from the
client's ERP. Generate a checklist the team can use with each new client:

```
## ERP Integration Checklist

### Step 1: Discovery (Day 1-3 of client onboarding)
[ ] Which ERP system does the client use? (SAP / 金蝶 / 用友 / Other)
[ ] Does the ERP have a REST API? If yes, what authentication method?
[ ] If no API: is database-level read access available? Via what protocol?
[ ] Is there an existing data export pipeline (e.g., daily CSV export)?
[ ] Who is the client-side technical contact for integration?

### Step 2: Minimum Data Requirements (MVP)
The following two data sets are the minimum needed to start the OODA loop:

Inventory Snapshot (pulled hourly or daily):
  [ ] Product identifier (SKU or item code)
  [ ] Product description / grade / specification
  [ ] Current quantity on hand
  [ ] Unit of measure
  [ ] Warehouse / location
  [ ] Average cost / last purchase price
  [ ] Date of last movement

Open Orders (pulled hourly or daily):
  [ ] Order ID
  [ ] Order type (purchase / sales)
  [ ] Product identifier
  [ ] Quantity ordered / quantity delivered
  [ ] Expected delivery date
  [ ] Counterparty (supplier or customer ID)
  [ ] Order status

### Step 3: Enhanced Data (Phase 2, adds significant Orient quality)
  [ ] Historical orders (last 12 months) — for demand pattern learning
  [ ] Supplier master data — reliability scores, lead times, contacts
  [ ] Customer master data — industry, credit terms, strategic importance
  [ ] Contract data — pricing mechanism, delivery commitments, validity dates

### Step 4: Integration Implementation Options (choose by client situation)
  Option A — REST API pull (preferred): 
    Schedule hourly GET requests; map response fields to internal schema
  Option B — Database read replica: 
    Read-only DB user; SQL queries on agreed tables; schedule with cron
  Option C — File-based (fallback): 
    Client exports CSV/Excel daily; SFTP or shared folder ingestion pipeline
  Option D — Middleware (complex ERP): 
    Use ERP vendor's integration middleware (e.g., SAP PI/PO, 金蝶 BOS)

### Step 5: Data Quality Validation
Before going live, validate:
  [ ] Inventory quantities reconcile with client's known totals (±2% tolerance)
  [ ] Order statuses match client's manual check on 10 sample orders
  [ ] Product codes are consistent (no duplicates, no missing mappings)
  [ ] Date fields are in expected timezone and format
```
