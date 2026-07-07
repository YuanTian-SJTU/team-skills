---
name: collaboration-dialogue-archive
description: |
  Use this skill when the user wants to record, live-capture, structure, summarize,
  archive, or synthesize conversations with collaborators, stakeholders, executives,
  investors, product leaders, engineers, customers, domain experts, ecosystem partners,
  or internal teams. Especially useful for a CTO or technical leader building an
  AI-native business platform who needs to preserve dialogue context while a
  conversation is still unfolding, extract strategic assumptions, decisions,
  disagreements, product insights, architecture implications, data opportunities,
  AI-native hypotheses, risks, and follow-up actions. Trigger on requests such as
  "一边聊一边记录", "边对话边归档", "访谈陪跑", "我说对方说",
  "记录我和某人的对话", "整理这次访谈", "归档会议记录", "总结合作者观点",
  "沉淀成战略输入", "提炼AI原生平台启发", or "汇总多位合作者的共识和分歧".
---

# Collaboration Dialogue Archive

## Purpose

Capture collaborator conversations as structured strategic memory for an AI-native business platform.

Do not default to generic meeting minutes. Preserve what was said, why it matters, where people disagree, which assumptions are hidden, and how the conversation affects business, product, technical, and data-layer decisions.

## Language

Use the user's language. For Chinese source material, produce Chinese archives.

## Workflow

## Live Capture Mode

Use this mode when the user wants to record a two-person interview while it is happening, not after the full transcript is complete. One participant is always the user. The other participant is the collaborator/interviewee.

### Start the Live Capture

At the start, ask for exactly these fields if the user has not provided them:

- Interviewee name
- Interviewee title or role
- Core topic of this interview
- Purpose of this interview

If the user has already provided enough context, start immediately. Do not ask a long setup questionnaire.

Opening prompt example:

```markdown
请先告诉我四件事：
- 对方姓名：
- 对方职位/角色：
- 本次访谈核心：
- 本次访谈目的：
```

### Speaker Labels

Expect the user to provide live input using speaker labels:

- `我说：...` means the user spoke.
- `对方说：...` means the interviewee spoke.
- If the user says they are using recording/transcription, interpret the user's own recording as `我说` and the other person's recording as `对方说`.

If speaker labels are missing but the speaker is obvious, infer cautiously. If ambiguous, ask one short clarification.

### During the Conversation

After each user message containing conversation content:

1. Append a short incremental capture under `现场记录`, preserving whether the content came from `我说` or `对方说`.
2. Extract only newly observed facts, opinions, assumptions, risks, and action items.
3. Keep the response compact so the user can continue the interview naturally.
4. When the latest meaningful content is from `对方说`, generate one recommended next question for the user to ask.
5. The next question should advance the interview purpose, probe assumptions, surface constraints, or clarify AI-native platform implications.
6. Do not generate the full archive unless the user asks to "收束", "整理成档案", "生成归档", "阶段小结", or similar.

Default live response format:

```markdown
已记录。

新增要点：
- {new point}
- {new point}

建议下一问：
- {one suggested question for the user to ask next}
```

If the user is speaking quickly or pasting many short fragments, use an even shorter response:

```markdown
已记录：{one-line summary}
建议下一问：{one question}
```

### Maintain a Running State

Internally maintain these buckets across turns:

- `基本信息`
- `现场记录`
- `我方发问与表达`
- `对方明确表达的观点`
- `用户判断或回应`
- `隐含假设`
- `分歧与张力`
- `AI原生平台启发`
- `风险与反证`
- `后续行动`
- `待确认问题`

When information changes, update the running state rather than treating each message as a separate archive.

### Periodic Summary

When the conversation becomes long or the user asks "现在小结一下", produce a short stage summary:

```markdown
## 阶段小结

- 当前主线：{summary}
- 已出现的关键观点：{points}
- 尚未确认的问题：{questions}
- 建议继续追问：{next questions}
- 可能的 AI 原生平台启发：{implications}
```

### Close the Capture

When the user says "收束归档", "生成完整归档", "整理成档案", or equivalent, produce the full archive using the standard archive structure below. Before finalizing, ask for missing high-value metadata only if it is essential, such as the participant role or whether sensitive information should be anonymized.

### 1. Identify the Conversation Context

Determine, infer, or mark as `未注明`:

- Date
- Participants and roles
- Organization or relationship to the user
- Conversation type
- Relation to the AI-native business platform
- Desired output depth: raw record, structured archive, action list, or synthesis

Conversation types:

- Strategic discussion
- Product discussion
- Technical architecture discussion
- Business model discussion
- Investor or board discussion
- Customer or user interview
- Partner or ecosystem discussion
- Internal alignment discussion
- Postmortem or decision review

### 2. Preserve the Raw Signal

Separate:

- Direct facts
- Participant opinions
- User interpretations
- Assistant inferences

Do not smooth over uncertainty, disagreement, emotion, or strong claims. If something is inferred, label it explicitly as `推断`.

### 3. Create the Archive Record

Use this default structure:

```markdown
# 对话归档：{主题}

## 基本信息

- 日期：{YYYY-MM-DD 或 未注明}
- 对话对象：{姓名 / 角色 / 组织}
- 对话类型：{类型}
- 关联主题：{产品 / 技术 / 商业 / 数据 / 组织 / 投资 / 客户}
- 重要程度：高 / 中 / 低
- 当前状态：待跟进 / 已形成决策 / 需再次确认 / 仅作背景记录

## 一句话摘要

{用 1-2 句话说明这次对话最重要的价值。}

## 背景

{为什么发生这次对话，对方站在什么位置，用户关心什么。}

## 关键观点

### 对方明确表达的观点

- {观点 1}
- {观点 2}

### 用户自己的判断或回应

- {判断 1}
- {判断 2}

### 隐含假设

- {假设 1}
- {假设 2}

## 分歧与张力

- {分歧点}
- {尚未解决的问题}
- {不同角色之间可能的利益或认知差异}

## 对 AI 原生商业平台的启发

### Business Layer

- {商业模式、市场定位、竞争壁垒、增长逻辑}

### Application Layer

- {产品形态、用户体验、人机协作方式、工作流重构}

### Technical Layer

- {模型、RAG、Agent、知识图谱、系统架构、集成方式}

### Data Layer

- {数据资产、数据闭环、知识结构、反馈飞轮}

## 决策影响

- 已影响的决策：{如有}
- 可能影响的决策：{如有}
- 需要暂缓的判断：{如有}

## 风险与反证

- {风险 1}
- {需要验证的反向证据}
- {不能过早相信的判断}

## 后续行动

- [ ] {行动项} / 负责人：{人} / 截止：{日期或未定}

## 可检索标签

`#合作者` `#AI原生平台` `#产品战略` `#技术架构` `#数据飞轮`
```

### 4. Classify Strategic Value

For each archive, assign one or more value buckets:

- `战略判断`
- `产品洞察`
- `技术架构`
- `组织协同`
- `市场验证`
- `风险预警`
- `待验证假设`

For a fuller taxonomy, read `references/archive-taxonomy.md`.

### 5. Synthesize Across Conversations

When the user provides multiple conversations or asks for aggregate insight, read `references/synthesis-patterns.md` and produce a cross-conversation synthesis.

## Decision Rules

- Prefer clarity over completeness when the source material is messy.
- Do not invent facts. Mark unknowns explicitly.
- Preserve disagreement instead of smoothing it away.
- Separate "what was said" from "what it means".
- Always extract implications for the AI-native business platform unless the user asks for a plain archive only.
- Turn strategic ambiguity into explicit hypotheses and validation questions.
- Turn execution detail into follow-up actions with owners and due dates when available.
- If the conversation includes sensitive people, companies, or negotiations, keep wording precise and avoid unnecessary speculation.
