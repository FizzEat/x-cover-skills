---
name: x-cover-node-workflow-window
description: X 长文封面图：节点工作流软件界面（工科蓝图与信息结构）。ComfyUI / n8n / Dify 类教程专用：密集连线的节点图 = 保姆级。 适用 AI 创作、AI 编程 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“节点工作流软件界面”风格时使用。
---

# 节点工作流软件界面

> ComfyUI / n8n / Dify 类教程专用：密集连线的节点图 = 保姆级。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | AI 创作、AI 编程 |
| 区域倾向 | 中文区优先 |
| 推荐画幅 | 16:9 出图，上传 X 长文前裁成 5:2，主体放中间 60% 安全区 |

## 工作流

1. 读用户给的长文标题、摘要或正文，提炼一句话核心观点和目标读者。
2. 把观点翻译成本风格能承载的画面：按下方“变量”逐个填空，变量必须是具体的可见物体，不写抽象词。
3. 输出 3 个版本：**稳妥版**（贴近模板）、**强钩子版**（放大冲突或尺度）、**反差版**（换一个意料之外的主体）。
4. 每个版本给出：中文画面说明一句 + 完整英文提示词 + 标题排版建议。
5. 按用户使用的模型补参数：Midjourney 末尾加 `--ar 16:9 --style raw`；FLUX / GPT-Image / Imagen 直接用自然语言并在开头写 `16:9 landscape`；即梦/豆包可把提示词翻成中文。
6. 提醒用户：画面里的文字一律后期排版，AI 只负责底图。

## PGVP 结构拆解

- **Identity 身份**：节点工作流深度实操封面
- **Spatial 空间**：左 35% 标题与特性徽章，右 65% 正面悬浮软件主界面
- **Visual State 终端视觉状态**：彩色贝塞尔连线连接十几个参数卡片，右上角小预览窗显示 [PREVIEW]
- **Material 材质响应**：墨黑磨砂界面，导线轻微霓虹反光
- **Lighting 光学**：界面自发光，背景暖灰柔光

## 提示词模板

```text
Modern tech tutorial cover, clean warm gray background. Left side reserved for title and small feature badge pills. Right side: a high-resolution dark mode desktop application window running a complex node graph editor, intricate colored bezier connector lines linking many parameter cards and text boxes, a small live preview panel showing [PREVIEW]. Node-based workflow UI, precise alignment, software dashboard aesthetic, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[PREVIEW]` | 预览窗口里的生成结果，如 an expressive 3D character、a cinematic landscape frame |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 几何节点 | `geometry nodes, procedural modeling, instancing, modifier stack` |
| 平面设计 · 面板磁贴 Dashboard Tiles | `Analytics dashboard with tile-based layout, row of KPI stat cards on top, charts and tables filling equal rectangular panels below, dark mode, data dense but legible` |
| 动画 · UI 动效微交互 | `UI micro-interaction motion, button states loading transitions gesture hints, 150-400ms easing curve, clear semantics, low-power Lottie SVG vector` |
| 平面设计 · 仪表盘 Dashboard | `executive analytics dashboard on large monitor, KPI scorecards top row, line and bar charts below, dark theme, real-time data` |
| 平面设计 · Segoe UI / Open Sans / Lato（UI 三件套） | `Segoe UI Windows application window mockup, clean interface typography, light theme, readable form labels, native desktop app` |
| 平面设计 · 移动界面 Mobile App UI | `iOS mobile banking app screens set, tab bar navigation, card lists, biometric login, clean modern fintech interface` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
