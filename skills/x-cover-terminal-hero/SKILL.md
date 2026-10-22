---
name: x-cover-terminal-hero
description: X 长文封面图：暗色终端窗口英雄图（工科蓝图与信息结构）。一扇 macOS 暗色终端窗口当主角，命令行的“真实感”就是干货感。 适用 AI 编程、AI 观察 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“暗色终端窗口英雄图”风格时使用。
---

# 暗色终端窗口英雄图

> 一扇 macOS 暗色终端窗口当主角，命令行的“真实感”就是干货感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | AI 编程、AI 观察 |
| 区域倾向 | 国内外通用 |
| 推荐画幅 | 16:9 出图，上传 X 长文前裁成 5:2，主体放中间 60% 安全区 |

## 工作流

1. 读用户给的长文标题、摘要或正文，提炼一句话核心观点和目标读者。
2. 把观点翻译成本风格能承载的画面：按下方“变量”逐个填空，变量必须是具体的可见物体，不写抽象词。
3. 输出 3 个版本：**稳妥版**（贴近模板）、**强钩子版**（放大冲突或尺度）、**反差版**（换一个意料之外的主体）。
4. 每个版本给出：中文画面说明一句 + 完整英文提示词 + 标题排版建议。
5. 按用户使用的模型补参数：Midjourney 末尾加 `--ar 16:9 --style raw`；FLUX / GPT-Image / Imagen 直接用自然语言并在开头写 `16:9 landscape`；即梦/豆包可把提示词翻成中文。
6. 提醒用户：画面里的文字一律后期排版，AI 只负责底图。

## PGVP 结构拆解

- **Identity 身份**：命令行工具实操教程封面
- **Spatial 空间**：窗口居右偏下 60%，左侧放标题，窗口略微透视倾斜
- **Visual State 终端视觉状态**：暗色终端窗口里是彩色高亮的命令与进度条，光标闪烁，窗口后方有柔和渐变光斑
- **Material 材质响应**：磨砂深灰窗口，红黄绿控制按钮，等宽字体纹理
- **Lighting 光学**：窗口自发光，背景低照度渐变

## 提示词模板

```text
Modern developer tool cover, deep [BG_COLOR] gradient background with a soft glow orb. A floating dark mode macOS terminal window in slight 3D perspective on the right, showing syntax-highlighted command lines, a progress bar and a blinking cursor (text as abstract texture), red yellow green window buttons, subtle glassmorphism reflection, clean left negative space for headline, crisp UI render, premium dev-tool landing page aesthetic, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[BG_COLOR]` | 背景主色，如 navy、charcoal、deep violet |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · UI 动效微交互 | `UI micro-interaction motion, button states loading transitions gesture hints, 150-400ms easing curve, clear semantics, low-power Lottie SVG vector` |
| 平面设计 · 面板磁贴 Dashboard Tiles | `Analytics dashboard with tile-based layout, row of KPI stat cards on top, charts and tables filling equal rectangular panels below, dark mode, data dense but legible` |
| 平面设计 · 极简瑞士回潮 Neo-Swiss Minimal | `Neo-Swiss minimalist poster, single Helvetica family only, extreme asymmetric grid, huge white margins, one small bold element, restrained monochrome with one accent color, gallery aesthetic` |
| 三维渲染 · 屏幕自发光作主光 | `screen light, phone glow, self-lit display key, monitor glow` |
| 平面设计 · Segoe UI / Open Sans / Lato（UI 三件套） | `Segoe UI Windows application window mockup, clean interface typography, light theme, readable form labels, native desktop app` |
| 平面设计 · 仪表盘 Dashboard | `executive analytics dashboard on large monitor, KPI scorecards top row, line and bar charts below, dark theme, real-time data` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
