# Data Layer Analysis Guide

## Purpose
Design the data strategy that will become the AI product's deepest competitive moat.
This guide covers data asset diagnosis, ontology design for technical users, knowledge
engineering pipelines, and data flywheel architecture.

---

## 1. Data Asset Diagnosis

Before designing anything, assess what the user actually has.

**Data Asset Scorecard**

Evaluate the user's data along five axes and assign Low/Medium/High:

| Axis | Low | Medium | High |
|------|-----|--------|------|
| Volume | <1GB text | 1-100GB | >100GB |
| Exclusivity | Publicly available | Aggregated/licensed | Proprietary only |
| Quality | Raw, noisy, unlabeled | Partially cleaned | Clean, labeled |
| Coverage | Partial domain coverage | Most topics covered | Comprehensive |
| Freshness | >1 year stale | Updated quarterly | Updated daily/weekly |

A high-moat data asset scores Medium or High on Exclusivity + Coverage + Freshness.
Volume matters less than most teams assume; a focused 1GB of high-quality exclusive
data often beats 100GB of generic public data.

**Strategic Data Questions**
- What data do you generate as a by-product of your product that competitors don't have?
- What data do your users create within your product that stays with you?
- What data partnerships or licensing opportunities exist in your domain?

---

## 2. Ontology Design

### When to Build an Explicit Ontology

Apply this decision rule before committing to ontology work:

**Build an explicit ontology if any of the following are true:**
- Domain has >50 distinct entity types with complex interrelationships
- Users need multi-hop reasoning ("find all suppliers who supply components used in
  products sold to regulated industries in Germany")
- Pure vector retrieval recall rate is below 70% on domain-specific queries
- The domain has well-established taxonomies (medical ICD codes, legal citation structures,
  financial instrument hierarchies) that define domain expertise
- Compliance requires traceable, explainable reasoning paths

**Don't build an explicit ontology if:**
- The domain is general-purpose (general knowledge, general writing assistance)
- Query patterns are mostly single-hop (find document about X)
- Team has no knowledge engineering experience and timeline is short
- Embedding + reranking achieves acceptable retrieval quality

### Ontology Design Levels

**Level 1 — Lightweight Taxonomy**
What it is: A classification tree of entity types, with no formal axioms.
Implementation: JSON/YAML taxonomy file; used to tag and filter documents.
Use when: You need structured faceted search; RAG filtering by entity type;
          consistent labeling across a large document corpus.
Tooling: Custom; can be generated with LLM assistance and human review.

Example structure:
```
Domain: Legal Documents
  └── Contract Types
      ├── Employment Contract
      │   ├── Full-time
      │   └── Contractor
      ├── NDA
      └── SLA
  └── Parties
      ├── Individual
      └── Legal Entity
  └── Clauses
      ├── Liability
      ├── Termination
      └── Governing Law
```

**Level 2 — Property Graph Schema**
What it is: Entities + directed relationships + typed properties; no formal axioms.
Implementation: Node and edge schema in Neo4j, TigerGraph, or Amazon Neptune.
Use when: Multi-hop queries matter; recommendation ("related contracts") is a feature;
          domain has rich relationship types that matter for reasoning.

Graph schema design process:
1. List 10-20 core entity types (nouns in the domain)
2. List 10-20 core relationship types (verbs between entities)
3. Assign typed properties to each entity and relationship
4. Validate with domain experts that the schema covers common query patterns
5. Build a small hand-curated sample (50-100 nodes/edges) for validation

**Level 3 — OWL Ontology**
What it is: Formal axioms; class hierarchies with inheritance; inference rules;
           enables automated reasoning (entailment).
Implementation: OWL 2 + reasoner (HermiT, Pellet); SPARQL for querying.
Use when: Regulatory/compliance domain where formal inference is required
          (healthcare, legal, pharmaceutical, finance with strict classification rules);
          integration with industry-standard ontologies (SNOMED, FIBO, schema.org);
          need to detect contradictions or infer implicit facts from explicit ones.

Note: Level 3 is expensive in engineering time and maintenance. Only choose it when
the business value of formal inference is demonstrably higher than the alternative.

---

## 3. Connecting Ontology to RAG

### Pattern 1: Metadata-Filtered RAG
Level: 1 (Taxonomy)
How: Tag each document chunk with ontology entities at indexing time.
     At query time, extract entities from user query and pre-filter vector search.
Result: Dramatically reduces false-positive retrievals in large corpora.

### Pattern 2: Structured Retrieval (Graph-Augmented RAG)
Level: 2 (Property Graph)
How: At query time, first query the knowledge graph for relevant entities and their
     relationships, then retrieve text chunks associated with those entities.
Result: Enables multi-hop retrieval that pure vector search cannot do.
     Example: "What are the risks of the contracts we have with suppliers of
               components classified as dual-use?" — requires traversing entity
               relationships before retrieving documents.

### Pattern 3: Graph RAG (Microsoft Research Pattern)
Level: 2 or 3
How: Build hierarchical summaries of graph communities at indexing time:
     entity summaries → community summaries → global summaries.
     At query time, retrieve at the appropriate granularity level.
Result: Global questions ("what are the main themes across all our contracts?")
     become answerable through the community summaries rather than chunk retrieval.

### Pattern 4: Hybrid (Dense + Sparse + Graph)
Recommended for production systems with Level 2 ontologies:
1. Vector search for semantic similarity
2. BM25 for keyword/entity match
3. Graph traversal for relationship-based retrieval
4. Reranker combines all signals into final ranked list

---

## 4. Ontology Engineering Path

**Step 1: Domain Expert Interviews**
Spend 2-4 hours with domain experts. Ask them to walk through typical reasoning
tasks and name the concepts they use. Record the vocabulary verbatim.
Output: raw concept list (expect 100-300 items)

**Step 2: LLM-Assisted Candidate Generation**
Feed the concept list to an LLM with this prompt structure:
"Given these domain concepts, identify: (a) entity types, (b) relationships between
entity types, (c) properties of each entity type. Format as a structured schema."
Output: draft schema (review carefully — LLMs will hallucinate relationships)

**Step 3: Human Review and Validation**
Present draft schema to domain experts. Check:
- Are any important entity types missing?
- Are any relationships incorrect or too granular?
- Does the schema cover the top 20 query patterns users will actually run?

**Step 4: Sample Population**
Manually populate 50-100 nodes/edges from real data. This forces schema refinement
and reveals ambiguities that theoretical design misses.

**Step 5: Automated Extraction Pipeline**
Build an LLM-based entity and relationship extraction pipeline to populate the
ontology at scale. Use the hand-curated sample as a few-shot training set.
Evaluate extraction precision/recall on a held-out validation set.

**Step 6: Versioning and Evolution**
Treat the ontology schema like a database schema — version controlled, migration-managed.
Define a governance process for adding new entity types (who approves, how to backfill).

---

## 5. Data Flywheel Design

This is the mechanism that makes the data moat compound over time.

**Flywheel Architecture**

```
User Interaction
      ↓
Signal Capture (implicit + explicit feedback)
      ↓
Signal Pipeline (deduplication, quality filtering, PII removal)
      ↓
Dataset Construction (fine-tuning data, eval data, RLHF data)
      ↓
Model Improvement (fine-tuning, prompt optimization, RAG corpus update)
      ↓
Better Product Experience
      ↓
More User Interaction ← (loop back)
```

**Flywheel Speed Factors**
- Signal density: how many useful signals per user session?
- Pipeline automation: is the path from signal to model update automated?
- Feedback latency: how quickly does a model improvement reach production?
- Signal quality: are the captured signals actually informative for model improvement?

**Practical Starting Point**
Before building the full flywheel, identify the single highest-value signal:
the user action that most strongly indicates "the AI was right/wrong."
Instrument only that signal first. Build the pipeline to process it. Prove the
loop closes before investing in comprehensive signal capture.

---

## 6. Data Governance and Compliance

**Training Data Compliance**
- Audit the provenance of all data used for fine-tuning or RAG corpus
- For user-generated data used for training: ensure ToS covers this use
- For licensed data: verify training use rights explicitly
- For web-scraped data: assess copyright risk by jurisdiction

**Data Residency Architecture**
If data must stay on-premise or within a region:
- RAG corpus: hosted in compliant cloud region or on-premise vector DB
- Fine-tuning: run training jobs in compliant environment
- Inference: either self-hosted or use model providers with regional data centers

**PII Handling in AI Pipelines**
- Scrub PII before indexing into RAG corpus
- Scrub PII before using interaction data for model training
- Log PII access separately with tighter access controls
- Define retention policies for interaction logs

---

## Output for Data Layer

Produce a structured summary:
1. Data Asset Scorecard: scores on 5 axes + strategic interpretation
2. Ontology Decision: Level chosen (0/1/2/3) + justification
3. Ontology Design: top-level entity types and relationships (if Level 1 or 2)
4. RAG Integration Pattern: which pattern applies + implementation notes
5. Flywheel Design: key signal + pipeline sketch + estimated loop latency
6. Compliance Notes: relevant risks + mitigation approach
