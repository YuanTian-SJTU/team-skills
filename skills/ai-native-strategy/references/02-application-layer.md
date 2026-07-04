# Application Layer Analysis Guide

## Purpose
Define the product form and interaction paradigm of the AI-native product.
The application layer translates the transformation thesis into what users
actually experience — and determines whether the product feels genuinely new
or like a chatbot bolted onto existing software.

---

## 1. Product Archetype Matrix

Help the user classify their product into one or more archetypes.
Each has distinct UX patterns, trust requirements, and feedback loop designs.

| Archetype | Core Pattern | Example Domains | Trust Requirement |
|-----------|-------------|----------------|-------------------|
| **Copilot** | AI alongside human workflow; human decides | Writing, coding, legal review | Medium — user stays in control |
| **Autopilot** | AI executes autonomously; human supervises | Data processing, monitoring, scheduling | High — errors have real consequences |
| **Oracle** | AI answers questions; human acts on answers | Research, diagnosis support, investment screening | Very high — advice quality is the product |
| **Generator** | AI produces artifacts; human selects/edits | Design, content, code, reports | Medium — output is a starting point |
| **Agent** | AI plans and executes multi-step tasks | Operations, customer service, research workflows | Very high — actions have side effects |

Most real products are hybrids. Help the user identify the primary archetype
and note which secondary archetypes apply in which contexts.

---

## 2. Human-AI Collaboration Mode

The collaboration mode determines the UX architecture and the error recovery design.

**Dimension 1: Initiative**
- AI-initiated: AI acts first, user reviews (Autopilot, Agent)
- User-initiated: user asks, AI responds (Copilot, Oracle)
- Mixed: AI proactively surfaces insights, user can also query directly

**Dimension 2: Override Granularity**
- No override: AI decisions are final (rare; only for low-stakes automation)
- Bulk override: user can undo entire AI action
- Step-level override: user can modify individual steps in an AI plan
- Continuous steering: user adjusts AI behavior in real-time

Help the user define the collaboration mode for each major user workflow.
The interaction model should feel like the natural inverse of whatever was
broken in the old paradigm — if the old way required 10 hours of expert time,
the new way should compress that into 10 minutes of AI-assisted review.

---

## 3. Trust Architecture

For investor/CEO audiences, trust architecture is a risk mitigation story.
For users, it's the difference between adoption and abandonment.

**Trust-Building Patterns**

1. **Source Attribution**: Always show where the AI's answer came from.
   When to use: Oracle and Copilot archetypes; any domain where accuracy is critical.

2. **Confidence Signals**: Surface uncertainty explicitly rather than hiding it.
   Design principle: a confident wrong answer destroys trust faster than an uncertain
   right answer. Never let the AI sound more confident than it is.

3. **Graceful Degradation**: When AI fails or is uncertain, fall back to a useful
   human-assisted path rather than returning an error.

4. **Audit Trail**: For regulated industries or high-stakes decisions, log what the
   AI reasoned, with what inputs, at what time. This is a compliance feature and
   a trust feature simultaneously.

5. **Human Escalation Path**: Always provide a clear path to human review.
   The AI-native product that removes human escalation entirely will face regulatory
   and adoption friction; the one that makes escalation smooth builds trust faster.

---

## 4. Feedback Loop Design

This is where the data flywheel becomes real. The application layer must be
designed to capture the signals that improve the AI over time.

**Signal Types by Archetype**

| Archetype | Primary Signal | Secondary Signal |
|-----------|---------------|-----------------|
| Copilot | Edit distance from AI suggestion to final output | Acceptance/rejection rate |
| Autopilot | Error correction rate; override frequency | Task completion rate |
| Oracle | User follow-through on AI recommendations | Explicit thumbs up/down |
| Generator | Selection and edit patterns | Regeneration frequency |
| Agent | Task success rate; step-level interventions | Time-to-completion vs manual |

Help the user identify: which signals will they capture from Day 1, and what
pipeline will translate those signals into model improvement? This is the flywheel.
The faster the loop, the stronger the moat.

---

## 5. Onboarding & Habit Formation

AI-native products have a unique onboarding challenge: users must form new
mental models, not just learn a new UI.

**The "First Wow" Moment**
Identify the single interaction where the user first thinks "this is genuinely
different from anything I've used before." Everything in onboarding should lead
to this moment as fast as possible, ideally within the first 5 minutes.

**Progressive Automation**
Don't start with full autopilot. Start with the user in control, let the AI
suggest, earn trust through suggestion quality, then gradually hand more
initiative to the AI as the user's confidence grows. This mirrors how humans
delegate to a new employee — they don't hand over full authority on Day 1.

**The Switching Cost Investment**
Identify what data or configuration the user "deposits" into the product that
makes it more valuable over time and harder to leave. This could be:
- Their personal writing style learned by the AI
- Their organization's internal knowledge ingested
- Their workflow patterns that the AI has optimized around

---

## Output for Application Layer

Produce a structured summary:
1. Primary product archetype + secondary archetypes by context
2. Collaboration mode definition (initiative + override granularity)
3. Trust architecture: which 2-3 patterns apply and why
4. Feedback loop: key signals + improvement pipeline sketch
5. Onboarding path: first wow moment + progressive automation plan

---

## Execution-Level Supplement (generate when user requests after Application Layer analysis)

This section is for product teams that need to move from product vision to
actionable design specifications. Generate three documents as separate files.

---

### Supplement A: User Stories

Generate 5-8 user stories per user type identified in the analysis.
Use this format for each story:

```
Story ID: [US-XX]
User Type: [e.g., 供应链总监 / 计划员 / 高管]
Job-to-be-done: As a [user type], when [situation/trigger], I want to [action],
                so that [outcome/value].

Acceptance Criteria:
  [ ] [Specific, testable condition 1]
  [ ] [Specific, testable condition 2]
  [ ] [Specific, testable condition 3]

Priority: [Must-have MVP / Should-have / Nice-to-have]
Notes: [Edge cases, constraints, open questions]
```

Focus on:
- Stories that directly implement the "active partner" interaction model
- Stories that capture the feedback signals for the data flywheel
- Stories that build trust (showing reasoning, expressing uncertainty)
- The "first wow moment" story — what must work perfectly from Day 1

Organize stories by user type. For each user type, the first story should be
the one that delivers the "first wow moment" for that user.

---

### Supplement B: Main User Flow

Generate a step-by-step flow for the most critical user journey:
**From receiving an AI-initiated alert → to completing the decision → to the
system recording the outcome.**

Format as a sequence with explicit decision points and branching paths:

```
## Main Flow: AI Alert → Decision → Outcome

### Trigger
[What causes the system to initiate contact — which signal, which threshold]

### Step 1: Notification Delivery
- Channel: [e.g., 企业微信机器人]
- Who receives it: [user role + routing logic]
- Content shown at this step: [exact fields visible in the notification]
- User actions available: [tap to open / dismiss / snooze]

### Step 2: Alert Detail View
- Screen/interface: [describe what the user sees]
- Content: [notification summary / impact assessment / confidence indicator]
- User actions available: [view full reasoning / accept / modify / reject / delegate]

### Step 3a: User Accepts the Recommendation
- What happens immediately: [system records acceptance + triggers Act]
- What confirmation does user see: [confirmation message]
- What happens in background: [audit log entry / outcome monitoring scheduled]

### Step 3b: User Modifies the Recommendation
- What editing interface appears: [which fields are editable]
- After editing, user submits: [what gets saved — both AI version and user version]
- Flywheel signal captured: [edit delta, modified fields, reason if provided]

### Step 3c: User Rejects the Recommendation
- Does the system ask for a reason? [yes/no, and if yes, what options]
- What is recorded: [rejection + reason category]
- Flywheel signal captured: [rejection signal + reason]

### Step 4: Outcome Tracking
- When: [24h / 48h / 72h after decision — depends on action type]
- What the system checks: [which metric, from which data source]
- How result is written back: [to which entity in the knowledge graph]
- Does user see the outcome? [yes — in a follow-up message / no]

### Edge Cases
- User does not open the notification within X hours: [what happens]
- System confidence is below threshold: [modified flow]
- User is unavailable (out of office): [escalation path]
- ERP data is stale at the time of alert: [degraded flow]
```

---

### Supplement C: Notification Specification

For each notification level defined in the analysis, produce an exact specification:

```
## Notification Spec: Level [1/2/3/4]

### Trigger Conditions
[Exact conditions that qualify a signal for this level — be specific about
thresholds, combinations, and time constraints]

### Recipients
- Primary: [role(s)]
- Secondary (if primary unresponsive after X minutes): [role(s)]
- Blackout hours: [times when this level is NOT sent, or held for next window]

### Channel
- Primary channel: [e.g., 企业微信群机器人 / 个人消息 / 系统内通知]
- Fallback channel (if primary fails): [e.g., SMS]

### Message Format
Title (max [N] characters):
  Template: "[emoji if applicable] [signal type]: [one-line impact]"
  Example: "⚠️ 价格预警：螺纹钢今日下行2.1%，影响3份在手合同"

Body (max [N] characters):
  Template: "[impact summary]\n建议：[recommended action]\n置信度：[X]%"
  Example: "当前持仓312吨，浮亏约¥18,600。建议与客户B确认交货节奏。\n置信度：74%"

Action Buttons (max 3):
  Button 1: "[label]" → [what it does]
  Button 2: "[label]" → [what it does]
  Button 3: "[label]" → [what it does, if applicable]

### Aggregation Rules
- If [N] notifications of this level queue within [X] minutes: [aggregate into one / send individually]
- Daily cap per user: [max N notifications of this level per day]
- If cap reached: [hold remaining for daily digest / escalate to next level / drop]

### Dismissal Behavior
- User dismisses without reading: [recorded as dismiss signal / no signal]
- User reads but takes no action after [X] hours: [follow-up? / record as low-urgency signal]
```

Generate this spec for each notification level (typically 3-4 levels based on the
urgency framework defined in the Application Layer analysis.
