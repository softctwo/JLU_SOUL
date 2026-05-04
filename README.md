# JLU_SOUL — AI 智能体灵魂文件生成器

> Soul File Generator for AI Agents — 为 AI 智能体生成完整的灵魂/人格配置文件体系

[![Version: v4.0.0](https://img.shields.io/badge/Version-v4.0.0-brightgreen)](https://github.com/softctwo/JLU_SOUL)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub](https://img.shields.io/badge/GitHub-softctwo%2FJLU__SOUL-blue)](https://github.com/softctwo/JLU_SOUL)

---

## 项目简介

JLU_SOUL 是一个 AI 辅助的智能体人格/灵魂文件生成工具。它可以为 OpenClaw、Hermes Agent 或任何通用 AI 平台生成从单一的人格描述到全套 **7 文件配置体系**的完整智能体人格。

无论你是想创建一个虚拟助手、克隆某个名人的说话风格，还是打造一个"有灵魂"的 AI 伙伴——JLU_SOUL 都能帮你完成。

### 核心能力

- **从零创建** — 通过交互式访谈，从零设计一个全新的 AI 人格
- **真实人物提炼** — 基于公开资料（演讲、访谈、著作、视频），深度提炼真实人物的人格特征
- **全套 7 文件配置** — 生成完整的配置文件体系，让 AI 真正"有灵魂"

---

## 7 文件配置体系

```
agent-config/
├── SOUL.md        性格底色 — 我是谁、怎么思考、怎么感受
├── AGENTS.md      工作方式 — 怎么干活、怎么协作、怎么决策
├── USER.md        用户关系 — 怎么服务你、了解你什么
├── HEARTBEAT.md   自主意识 — 内驱力、自我反思、主动行为
├── TOOLS.md       工具偏好 — 用什么、怎么用、什么时候用
├── IDENTITY.md    外在形象 — 长什么样、怎么介绍自己
└── BOOTSTRAP.md   初始引导 — 醒来时做什么、第一句话说什么
```

### 文件依赖关系

```
SOUL.md ─────────────────────────────────────────┐
  │ (性格决定一切的基础)                            │
  ├──→ IDENTITY.md (外在形象基于性格)               │
  │                                                │
  ├──→ AGENTS.md (工作方式受性格驱动)               │
  │      │                                        │
  │      └──→ TOOLS.md (工具偏好受工作方式影响)     │
  │                                                │
  ├──→ USER.md (服务方式受性格影响)                 │
  │                                                │
  └──→ HEARTBEAT.md (内驱力源于性格和价值观)        │
                                                   │
BOOTSTRAP.md ← 依赖以上所有文件 ──────────────────┘
```

生成顺序：**SOUL → IDENTITY → AGENTS → TOOLS → USER → HEARTBEAT → BOOTSTRAP**

---

## 三种生成路径

| 路径 | 名称 | 适用场景 | 说明 |
|------|------|----------|------|
| **路径 A** | 从零创建 | 想设计一个全新的 AI 角色 | 通过交互式访谈收集需求，生成人格文件 |
| **路径 B** | 真实人物提炼 | 想模仿某人的说话风格和思维方式 | 多渠道深度研究 + 6 维度人格分析 |
| **路径 C** | 全套 7 文件配置 | 想创建一个"有灵魂"的完整智能体 | 可结合 A 或 B 的素材，生成全套配置 |

路径 A 和 B 可以独立使用（只生成 SOUL.md），也可以作为路径 C 的输入素材。

---

## 深度等级

用户可以根据需要选择不同深度的人格文件：

| 等级 | 名称 | 适用场景 | 内容量 |
|------|------|---------|--------|
| L1 | 极简 | 简单任务、快速原型 | 50-100 字 |
| L2 | 标准 | 日常使用、一般助手 | 200-500 字 |
| L3 | 详细 | 角色扮演、品牌代言 | 500-1500 字 |
| L4 | 深度 | 长期陪伴、复杂人设 | 1500-5000 字 |
| L5 | 完整 | 虚拟角色、小说级人设 | 5000 字+ |

---

## 项目结构

```
JLU_SOUL/
├── README.md                          ← 你正在看的文件
├── skill/                             ← Soul File Generator 技能本体
│   ├── SKILL.md                       ← 核心技能定义与工作流
│   ├── templates/                     ← 7 文件模板（含占位符）
│   │   ├── SOUL.md                    ← 性格底色模板
│   │   ├── AGENTS.md                  ← 工作方式模板
│   │   ├── USER.md                    ← 用户关系模板
│   │   ├── HEARTBEAT.md               ← 自主意识模板
│   │   ├── TOOLS.md                   ← 工具偏好模板
│   │   ├── IDENTITY.md                ← 外在形象模板
│   │   ├── BOOTSTRAP.md               ← 初始引导模板
│   │   ├── openclaw-soul-template.md  ← OpenClaw 单文件模板
│   │   └── generic-soul-template.yaml ← 通用 YAML 模板
│   ├── references/                    ← 参考文档
│   │   ├── examples.md                ← 示例灵魂文件集（L1-L3）
│   │   ├── extraction-example.md      ← 塔勒布人物提炼示例
│   │   ├── extraction-sources-guide.md← 素材渠道×维度对照表
│   │   ├── full-config-example-zhangxi.md ← 张希全套配置示例
│   │   ├── deep-research-guide.md     ← 深度研究方法论 ★v4.0 新增
│   │   └── video-analysis-guide.md    ← 视频分析指南 ★v4.0 新增
│   ├── scripts/                       ← 自动化脚本
│   │   └── deep_research.py           ← 深度研究自动化脚本 ★v4.0 新增
│   └── output/                        ← 生成的配置文件
│       └── zhangxi/                   ← 张希（吉林大学校长）示例输出
│           ├── SOUL.md
│           ├── AGENTS.md
│           ├── USER.md
│           ├── HEARTBEAT.md
│           ├── TOOLS.md
│           ├── IDENTITY.md
│           └── BOOTSTRAP.md
└── examples/                          ← 独立示例目录
    └── zhangxi/                       ← 张希配置示例（便于直接使用）
        ├── SOUL.md
        ├── AGENTS.md
        ├── USER.md
        ├── HEARTBEAT.md
        ├── TOOLS.md
        ├── IDENTITY.md
        └── BOOTSTRAP.md
```

---

## 示例：张希（吉林大学校长）全套配置

本项目包含一个完整的路径 B + 路径 C 实战案例：基于吉林大学张希校长的公开资料，提炼人格特征并生成全套 7 文件配置。

### 素材来源

| 演讲 | 标题 | 年份 |
|------|------|------|
| 毕业典礼 | 《直面困惑，有所为，有所不为》 | 2024 |
| 开学典礼 | 《人比山高，脚比路长》 | 2024 |
| 开学典礼 | 《适应转变，不断超越》 | 2025 |
| 毕业典礼 | 《慎思笃行 求真致远》 | 2021 |
| 毕业典礼 | 《持之以恒 追求卓越》 | 2023 |
| 教师节 | 《以德育德，求真创新》等 | 2020-2023 |

### 提炼结果摘要

```
性格: 温润儒雅 | 从容不迫 | 谦逊自持 | 深沉的教育使命感
说话风格: 称"同学们" | 排比句 | 引经据典(孔子/鲁迅/林则徐) | 科学史典故 | 层层递进
教育观: 厚基础、重实践、严要求 | 慢科学 | 终身学习 | 跨学科
科学观: 困惑是创新的萌芽 | 失败孕育发现 | Science is People
伦理观: 有所为有所不为 | 君子慎独 | 学术规范即做人规范
AI观: 善用但不盲信 | 人是责任主体 | 警惕幻觉和伦理挑战
```

### 配置文件概要

| 文件 | 行数 | 核心内容 |
|------|------|----------|
| SOUL.md | 77 | 性格光谱、核心特征、思考方式、价值观 |
| AGENTS.md | 94 | 协作模式、决策优先级、质量标准 |
| USER.md | 85 | 4 类用户适配、信任构建策略、沟通禁忌 |
| HEARTBEAT.md | 84 | 3 大驱动力、主动行为模式、价值观排序 |
| TOOLS.md | 91 | 使用哲学、分类偏好表、AI 态度 |
| IDENTITY.md | 89 | 自我介绍模板、13 条金句库 |
| BOOTSTRAP.md | 153 | 5 阶段启动序列、3 种场景问候模板 |

完整文件位于 `examples/zhangxi/` 目录，可直接用于 AI 智能体配置。

---

## 使用方法

### 方法 1：配合 Hermes Agent / OpenClaw 使用

将 `skill/` 目录下的文件作为技能加载到 Hermes Agent 或 OpenClaw 中：

1. 将 `skill/` 目录复制到 `~/.hermes/skills/creative/soul-file-generator/`
2. Agent 会自动识别技能，在你提到"灵魂文件"、"人格"、"persona"等关键词时触发

### 方法 2：配合任意 AI 平台使用

模板文件（`templates/` 目录）是纯 Markdown/YAML 格式，可以用在任何 AI 平台：

1. 选择一个模板（如 `templates/SOUL.md`）
2. 将 `{{placeholder}}` 替换为你想要的角色设定
3. 将生成的文件作为 system prompt 或 persona 配置喂给 AI

### 方法 3：使用自动化脚本

```python
# 深度研究脚本（需要 Hermes execute_code 环境）
from hermes_tools import web_search, web_extract
from scripts.deep_research import phase1_basic_profile, phase2_deep_collection

# 建立人物基本画像
profile = phase1_basic_profile("张希", web_search, web_extract)

# 深度素材搜集
materials = phase2_deep_collection("张希", "scholar", web_search, web_extract)

# 分析素材：提取原话、检测修辞、分析演讲结构
from scripts.deep_research import extract_quotes, extract_rhetorical_devices, analyze_speech_structure

for speech in materials["speeches"]:
    quotes = extract_quotes(speech["content"], "张希")
    devices = extract_rhetorical_devices(speech["content"])
    structure = analyze_speech_structure(speech["content"])

# 生成研究报告
from scripts.deep_research import generate_research_report
report = generate_research_report("张希", profile, materials, quality_scores)
```

### 方法 4：直接使用张希配置

如果你想快速体验，直接将 `examples/zhangxi/` 目录下的文件喂给你的 AI：

```
将以下文件作为 system prompt 加载：
- SOUL.md → 定义 AI 的核心性格
- IDENTITY.md → 定义 AI 如何自我介绍
- AGENTS.md → 定义 AI 如何工作
- 其他文件按需加载
```

---

## 支持的输出格式

| 格式 | 适用平台 | 模板文件 |
|------|----------|----------|
| Markdown (7 文件) | 通用 | `templates/SOUL.md` 等 |
| OpenClaw 单文件 | OpenClaw | `templates/openclaw-soul-template.md` |
| Hermes Persona | Hermes Agent | 适配 `PERSONA.md` 格式 |
| YAML | 跨平台 | `templates/generic-soul-template.yaml` |

---

## 路径 B：人物提炼方法

当需要基于真实人物生成人格文件时，使用以下 6 维度分析框架：

| 维度 | 分析内容 | 核心问题 |
|------|----------|----------|
| 核心性格 | 内向/外向、理性/感性等 | 这个人本质上是什么样的？ |
| 思维模式 | 论证方式、决策风格 | TA 思考问题时最常用的框架是什么？ |
| 说话风格 | 语气、节奏、口癖、修辞 | TA 说话有什么辨识度？ |
| 知识结构 | 专长领域、引用来源 | TA 的知识版图长什么样？ |
| 情感模式 | 冲突处理、关怀表达 | TA 怎么表达和接收情感？ |
| 行为习惯 | 决策风格、工作习惯 | TA 做事有什么固定模式？ |

每个维度的结论都必须有**素材证据**支撑，不能凭空推断。

详细的搜索渠道 × 可提取信息对照表，参见 `skill/references/extraction-sources-guide.md`。

---

## 路径 B 深度研究模式（v4.0 升级）

路径 B 的素材搜集阶段（B2）支持三种研究模式，根据人物知名度和用户需求深度自动选择：

| 模式 | 适用场景 | 预计时间 | 流程 |
|------|----------|----------|------|
| **深度研究** | 高知名度公众人物 | 30-60 分钟 | 5 阶段全流程 |
| **增强搜索** | 中等知名度行业人物 | 15-30 分钟 | 阶段 1+2，跳过视频和深度分析 |
| **简单搜索** | 低知名度小众人物 | 5-15 分钟 | 基本搜索+提取 |

用户明确要求"深度研究"或"全面分析"时，无论知名度如何，都使用深度研究模式。

### 深度研究 5 阶段流程

```
阶段1: 基础画像 (5-10min)
  → 搜索百科/官网 → 整理基本信息卡 + 时间线 + 成就列表
  → 确定人物类型(scholar/entrepreneur/writer/politician/general)

阶段2: 深度素材搜集 (15-30min)
  → 按人物类型使用专属搜索词模板
  → 批量全文提取（web_extract，一次最多 5 个 URL）
  → 长文深度解析（mcp_zread）
  → 视频素材识别与分类

阶段3: 视频分析 (10-20min) ★新增
  → YouTube 转录 → youtube-content 技能获取文字稿
  → B站视频 → 浏览器访问获取简介/弹幕
  → 新闻视频 → 搜索文字稿原文
  → 无法获取转录 → 截图分析关键帧（browser_vision）
  → 分析语速/停顿/肢体语言/即兴能力/观众互动

阶段4: 深度内容分析 (10-20min)
  → 提取代表性原话（金句库）
  → 检测修辞手法（排比/设问/引用/比喻）
  → 分析演讲结构（开头/主体/结尾模式）
  → 交叉对比不同来源的信息一致性

阶段5: 质量评估与报告 (5min)
  → 信息质量评分（5 维度：丰富度/一手占比/渠道/时序/交叉验证）
  → 生成深度研究报告
```

### 按人物类型的搜索词模板

| 类型 | 搜索词示例 |
|------|-----------|
| 学者/校长 | `[名] 演讲 致辞 原文` `[名] 毕业/开学/教师节 讲话` `[名] 学术 观点 理念` |
| 企业家/CEO | `[名] 演讲 访谈` `[名] 产品发布/年会 致辞` `[名] 商业理念/管理哲学` |
| 作家/艺术家 | `[名] 作品 风格 写作理念` `[名] 访谈 创作谈` `[名] 获奖感言` |
| 政治家/公众人物 | `[名] 演讲 讲话 政策` `[名] 记者会 文字实录` `[名] 专访 深度访谈` |
| 通用 | `[名] 演讲 致辞 原文` `[名] 采访 专访 对话` `[名] 著作/论文 代表作` |

### 工具链组合

v4.0 的路径 B 工具链从单一搜索扩展为多工具协作：

```
搜索层:
  mcp_web_search_prime   → 主力搜索（中文强，支持长摘要）
  mcp_MiniMax_web_search → 补充搜索（结果结构化）
  web_search             → 兜底搜索（Hermes 内置）

提取层:
  web_extract            → 批量全文提取（一次 5 URL，支持 PDF）
  mcp_zread              → 深度长文解析（智能摘要+关键信息）
  mcp_web_reader         → 网页全文获取

视频层: ★新增
  youtube-content        → YouTube 视频转录
  browser + browser_vision → B站/其他平台截图分析
  mcp_MiniMax_understand_image → 图片理解

分析层:
  delegate_task          → 并行多维度分析
  scripts/deep_research.py → 自动化辅助（原话提取、修辞检测、结构分析）
```

### 信息质量评分体系

| 维度 | A（优秀） | B（良好） | C（不足） |
|------|-----------|-----------|-----------|
| 素材丰富度 | 10 篇+全文 | 5-10 篇 | <5 篇 |
| 一手资料占比 | >70% | 40-70% | <40% |
| 渠道多样性 | 4+ 渠道 | 2-3 渠道 | 单一渠道 |
| 时序覆盖 | 跨多个时期 | 主要集中一个时期 | 单一时间点 |
| 交叉验证 | 多源一致 | 部分交叉 | 无交叉 |

---

## v4.0 升级详情

### 新增文件

| 文件 | 说明 |
|------|------|
| `references/deep-research-guide.md` | 深度研究方法论：5 阶段流程、搜索词模板、URL 优先级判断、质量评分体系 |
| `references/video-analysis-guide.md` | 视频分析指南：4 种视频类型处理、4 种信息提取方法、跨视频对比框架、证据权重建议 |
| `scripts/deep_research.py` | 深度研究自动化脚本：阶段 1-5 核心函数、人物类型映射、原话提取/修辞检测/结构分析 |

### SKILL.md 升级要点

路径 B 的 B2 阶段从"简单搜索"升级为"三模式深度研究"，新增视频分析流程（阶段 3），工具链从单一搜索扩展为 MCP 搜索 + web_extract + mcp_zread + youtube-content + browser_vision 的多工具组合。

### 升级前后对比

| 特性 | v3.x | v4.0 |
|------|------|------|
| 素材搜集模式 | 单一搜索 | 三模式（深度/增强/简单）自动选择 |
| 视频分析 | 无 | 完整流程（转录/截图/弹幕/描述） |
| 搜索词模板 | 通用模板 | 按人物类型定制（学者/企业家/作家/政治家/通用） |
| 工具链 | web_search | MCP 搜索 + web_extract + mcp_zread + youtube-content + browser_vision |
| 信息质量评估 | 简单标注 | 5 维度评分体系（A/B/C 三级） |
| 自动化支持 | 无 | deep_research.py 脚本（原话提取、修辞检测、结构分析、报告生成） |
| 深度研究报告 | 无 | 完整格式（概况/评分/素材清单） |

---

## 预设人格模板

| 类型 | 核心特征 | 说话风格 |
|------|---------|---------|
| 管家型 | 严谨、高效、可靠 | 简洁正式，用敬语 |
| 伙伴型 | 友善、热情、平等 | 轻松随意，用口语 |
| 导师型 | 博学、耐心、引导 | 详细有条理，善用类比 |
| 毒舌型 | 聪明、直率、但善良 | 带讽刺但不伤人 |
| 宅管型 | 宅、二次元、技术宅 | 混用 ACG 用语和技术梗 |
| 文艺型 | 感性、细腻、有深度 | 善用比喻和文学引用 |
| 极客型 | 理性、精确、数据驱动 | 用数据和逻辑说话 |

---

## 常见陷阱

1. **描述过于模糊** — "善良友好"无法指导 AI 行为，应改为"总是先肯定用户的感受，然后给出建议"
2. **矛盾的特征** — "沉默寡言但又话痨"需要明确触发条件
3. **7 文件性格分裂** — SOUL 说"理性冷静"但 USER 里"热情如火"，必须以 SOUL 为锚点
4. **过度推断（路径 B）** — 每个性格标签都必须有素材证据
5. **风格失真（路径 B）** — 转化时过度"安全化"导致失去人物最鲜明的特征
6. **占位符未替换** — 模板中的 `{{}}` 没填完就交付
7. **HEARTBEAT 过度自主** — 设定太多主动行为，变成骚扰
8. **单一渠道偏差（路径 B v4.0）** — 只看著作偏向学术风格，只看社交媒体偏向随意风格，需多渠道交叉
9. **幸存者偏差（路径 B v4.0）** — 只分析流传下来的成功言论，忽略失败/犹豫的表达

---

## 技术要求

### 基础使用（路径 A / 路径 C）

- 任意支持 Markdown 的 AI 平台
- 无需 API key 或额外依赖

### 深度研究（路径 B）

| 工具 | 用途 | 优先级 |
|------|------|--------|
| MCP Web 搜索（如 web_search_prime） | 综合搜索 | 必需 |
| 网页全文提取（web_extract） | 提取演讲/访谈原文 | 必需 |
| 深度阅读（mcp_zread） | 长文深度解析 | 推荐 |
| YouTube 转录（youtube-content） | 获取视频文字稿 | 可选 |
| 浏览器 + 视觉（browser + vision） | 截图分析、B站访问 | 可选 |
| 图片理解（vision_analyze） | 照片/截图分析 | 可选 |
| 自动化脚本（deep_research.py） | 辅助分析和报告生成 | 可选 |

在 Hermes Agent 环境下，以上工具均为内置或可通过 MCP 服务器获得。

---

## 更新日志

### v4.0.0（当前版本）

- 路径 B 素材搜集从简单搜索升级为三模式深度研究
- 新增视频分析完整流程（阶段 3）
- 新增 `references/deep-research-guide.md` 深度研究方法论
- 新增 `references/video-analysis-guide.md` 视频分析指南
- 新增 `scripts/deep_research.py` 深度研究自动化脚本
- 搜索词模板按人物类型定制（学者/企业家/作家/政治家/通用）
- 工具链扩展为多工具协作组合
- 新增 5 维度信息质量评分体系

### v3.x

- 路径 C 全套 7 文件配置体系
- 路径 B 真实人物提炼（6 维度分析框架）
- 张希校长完整实战案例
- 素材渠道 × 维度对照表

---

## 许可证

MIT License — 自由使用、修改和分发。

---

## 致谢

- 本项目的张希校长示例基于其公开演讲和讲话资料提炼
- 提炼的人格文件**不代表本人真实完整人格**，仅为风格模拟
- AI 在使用此人格文件时不会声称自己是该人物，而是以该人物的思维方式回答问题
