---
name: ontology-kb
description: |
  Personal ontology knowledge base — captures inspirations, ideas, quotes, and fragments of thought with deep semantic structure. Use this skill whenever the user wants to: record an idea, insight, or quote; save a thought to their knowledge base; add a new entry; connect two ideas; search or browse their knowledge; reflect on a passage or reading; explore a thread of thought. 
  
  Also trigger when the user says phrases like "记录", "存入知识库", "记下来", "我有个想法", "这句话很好", "帮我整理一下", "我想到了", "查一下我的知识库", "这跟XXX有什么关联", or pastes a quote or excerpt and asks to save it.

  This skill is about making knowledge *live* — not just cataloguing facts, but capturing the reasoning, the context, the personal resonance, and the invisible threads between ideas. Every entry should know not just *what* it is, but *why it matters* and *how it connects*.
---

# 灵感本体知识库 (Ontology Knowledge Base)

## 哲学基础

这个知识库的核心思想是：知识不是孤立的事实，而是有生命的网络。每一个节点都应该回答三个问题：
- **是什么**（What）：这个想法/引用/观察是什么
- **为什么**（Why）：它为什么成立？背后的推理是什么？它为什么对我重要？
- **与什么相连**（How）：它如何与其他想法相互支撑、挑战或延伸

这是"本体"而非"数据库"的关键区别：本体捕捉的是关系的*类型*和*意义*，而不只是数据的存在。

---

## 知识库位置

知识库存放在用户的工作文件夹中，结构如下：

```
[工作文件夹]/知识库/
├── _schema.md          ← 本体定义（首次初始化时创建）
├── _index.md           ← 自动维护的节点总索引
└── nodes/              ← 所有知识节点
    └── YYYYMMDD-slug.md
```

如果 `知识库/` 目录不存在，**在第一次录入时初始化它**，并写入 `_schema.md` 和空的 `_index.md`。

---

## 知识节点类型（本体类）

| 类型 | 中文 | 用途 |
|------|------|------|
| `insight` | 洞见 | 用户自己产生的原创想法或突破性认识 |
| `quote` | 摘抄 | 来自书籍、对话、文章的引文 |
| `question` | 问题 | 值得长期探索的开放性问题 |
| `principle` | 原则 | 从经验或推理中提炼出的行动/认知准则 |
| `observation` | 观察 | 对现象的具体注意，尚未升华为洞见 |
| `synthesis` | 综合 | 将两个或多个已有节点联系起来的新发现 |

---

## 关系类型（本体属性）

节点之间的关系应有明确类型，不能只说"相关"：

| 关系 | 含义 |
|------|------|
| `supports` | A 为 B 提供论据或证据 |
| `challenges` | A 质疑或挑战 B |
| `extends` | A 是 B 的延伸或具体化 |
| `exemplifies` | A 是 B 的一个具体例子 |
| `contrasts` | A 与 B 形成有意义的张力或对比 |
| `inspires` | A 触发了对 B 的思考 |
| `synthesizes` | A 将 B 和 C 融合成了新理解 |

---

## 知识节点 YAML Schema

每个节点文件的 frontmatter：

```yaml
---
id: "YYYYMMDD-short-slug"          # 唯一 ID，用于跨文件引用
type: insight | quote | question | principle | observation | synthesis
title: "简洁的标题"
created: "YYYY-MM-DD"
source:                             # quote 类型必填，其他类型如适用也填
  origin: "来源名称（书名/人名/场合）"
  passage: "原文段落或页码"
  context: "遇到这个想法时的情境"
domain: []                          # 知识域标签，如 ["认识论", "AI", "设计"]
resonance: 3                        # 个人共鸣强度 1–5
status: seed | developing | mature  # 这个想法的成熟度
related: []                         # 见下方格式
---
```

`related` 的格式：
```yaml
related:
  - id: "20240101-some-idea"
    relation: supports              # 关系类型（见上表）
    note: "一句话说明为什么它们相连"
```

---

## 节点正文结构

```markdown
# [标题]

## 本体 (What)
[想法的核心陈述。如果是 quote，先放原文引用，再用自己的话重述其核心含义。]

## 所以然 (Why)

### 推理过程
[为什么这个想法是真的/重要的？它基于什么前提？支撑它的逻辑链是什么？]

### 个人反思
[我当时怎么想的？它让我感到什么？我有什么疑问或抵触？]

### 关联网络
[与其他节点的连接——用 [[节点ID]] 引用。每个连接都要说明*为什么*相连，连接的性质是什么。]

## 延伸问题
[这个想法让我产生了哪些新的问题？写成问句。]

## 应用场景
[这个想法可以如何在实际中使用、验证或检验？]
```

`延伸问题` 和 `应用场景` 如果暂时没有内容，可以留空或省略，但不要删除标题——它们是邀请未来的自己回来补充。

---

## 操作模式

### 模式 A：录入新知识

当用户说要记录一个想法、引用或观察时：

1. **理解输入**：用户直接描述，还是粘贴了原文？这是 insight、quote 还是 question？

2. **提炼结构**：
   - 用一句话概括核心（这将成为 `title`）
   - 识别来源（如果有）
   - 推断所属 `domain`
   
3. **追问"所以然"**（这是最重要的一步）：
   - 问用户："你为什么觉得这个重要？" 或 "这让你想到了什么？"
   - 如果用户已经说了理由，直接提炼；否则温和地问一个问题
   - **不要跳过这步**——没有"所以然"的知识节点只是数据，不是知识

4. **主动寻找关联**（索引优先策略）：
   - 先读 `知识库/_index.md`——扫描标题、domain 标签、一句话摘要，识别 3–5 个最有可能相关的节点 ID
   - 再读那几个候选节点的完整文件，判断关联类型和程度
   - 如果确认有关联：在**新节点** `related` 里写入旧节点的 id + relation + note；同时**打开旧节点文件，在其 `related` 字段末尾追加**指回新节点的对称条目（双向链接是强制要求，不可省略）
   - 如果没有找到关联：在新节点的 `related` 留空，但在 `### 关联网络` 正文里写一句"暂未发现关联节点，待知识库扩充后回顾"

5. **生成文件**：写入 `知识库/nodes/YYYYMMDD-slug.md`。同时更新 `_index.md`（追加新行，包含摘要列）。

6. **向用户确认**：简短告知已保存，如发现了有趣的关联，说出来。

### 模式 B：查询与探索

当用户说"帮我看看…"、"有没有关于…的内容"、"把相关的联系起来"时：

1. 先读 `_index.md`，从摘要列快速定位候选节点（不要盲目读所有文件）
2. 读候选节点完整内容，**沿着 `related` 字段递归遍历关系图**，找到二级、三级连接
3. 呈现一个关系地图：核心节点 + 它的支撑/挑战/延伸，标注每条连接的性质
4. 主动提出：这些节点之间是否可以生成一个新的 `synthesis` 节点？

### 模式 C：更新已有节点

当用户说"我对XX有了新的想法"、"上次那条记录可以补充一下"时：

1. 找到对应节点
2. 在 `个人反思` 或 `延伸问题` 中追加新内容（用日期标注）
3. 如果是重要更新，把 `status` 从 `seed` 升级到 `developing` 或 `mature`

---

## 风格原则

- **用用户自己的语言**：title 和反思部分应该听起来像用户说话，不是学术摘要
- **宁少勿滥**：一个有深度"所以然"的节点，好过十个只有"本体"的节点
- **关联是财富**：每次录入都要主动搜一遍已有节点，哪怕只是浏览标题
- **问题是知识**：`延伸问题` 部分同样重要——未解答的好问题是知识库最有价值的部分之一
- **为AI伙伴写作**：正文应该足够自解释，让一个没有上下文的 AI 读完也能理解这个想法的背景和意义

---

## 初始化知识库

如果 `知识库/` 不存在，首次运行时创建它，并写入：

**`_schema.md`**：复制本技能的本体定义（类型表、关系表、schema）作为知识库的说明书

**`_index.md`**：
```markdown
# 知识库索引

最后更新：YYYY-MM-DD

## 节点总览

| ID | 标题 | 类型 | 域 | 摘要（一句话） | 成熟度 | 创建日期 |
|----|------|------|----|----------------|--------|----------|
```

每次添加或更新节点后，自动在索引里追加/更新对应行。**摘要列是关键**——用一句话抓住节点的核心主张，不是复述标题。Claude 查询关联时会先读这一列来判断哪些节点值得深读，所以摘要质量直接影响关联发现的准确性。
