---
name: collaboration-dialogue-archive
description: |
  Use this skill when the user wants to record, structure, summarize, archive, or synthesize
  conversations with collaborators, stakeholders, executives, investors, product leaders,
  engineers, customers, domain experts, ecosystem partners, or internal teams. Especially
  useful for a CTO or technical leader building an AI-native business platform who needs to
  preserve dialogue context, extract strategic assumptions, decisions, disagreements,
  product insights, architecture implications, data opportunities, AI-native hypotheses,
  risks, and follow-up actions. Trigger on requests such as "记录我和某人的对话",
  "整理这次访谈", "归档会议记录", "总结合作者观点", "沉淀成战略输入",
  "提炼AI原生平台启发", or "汇总多位合作者的共识和分歧".
---

# Collaboration Dialogue Archive

## Purpose

Capture collaborator conversations as structured strategic memory for an AI-native business platform.

Do not default to generic meeting minutes. Preserve what was said, why it matters, where people disagree, which assumptions are hidden, and how the conversation affects business, product, technical, and data-layer decisions.

## Language

Use the user's language. For Chinese source material, produce Chinese archives.

## Workflow

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
