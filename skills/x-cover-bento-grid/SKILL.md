---
name: x-cover-bento-grid
description: X 长文封面图：Bento 便当格功能总览（工科蓝图与信息结构）。一张图塞下 6~8 个要点，苹果发布会式 Bento 网格，适合“合集/全解析”。 适用 AI 编程、AI 观察、做号变现 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“Bento 便当格功能总览”风格时使用。
---

# Bento 便当格功能总览

> 一张图塞下 6~8 个要点，苹果发布会式 Bento 网格，适合“合集/全解析”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | AI 编程、AI 观察、做号变现 |
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

- **Identity 身份**：功能全景总览封面
- **Spatial 空间**：非对称 Bento 网格，一大格主视觉 + 5~7 个小格
- **Visual State 终端视觉状态**：主格是 [HERO_OBJECT]，小格分别是图标、迷你图表、开关、数字卡
- **Material 材质响应**：磨砂亚克力卡片，大圆角，柔和分层阴影
- **Lighting 光学**：柔和渐变底，玻璃边缘高光

## 提示词模板

```text
Asymmetric bento grid layout infographic, landscape. One large hero tile featuring [HERO_OBJECT], surrounded by 6 smaller rounded tiles with minimal line icons, a tiny bar chart, a toggle switch, a big number placeholder and a short label placeholder. Frosted acrylic glass tiles with 24px rounded corners, soft layered shadows, 90% neutral colors with [ACCENT] accent, Apple keynote feature-overview aesthetic, generous gutters, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[HERO_OBJECT]` | 核心主体，如 a glossy 3D AI chip、a glass app icon |
| `[ACCENT]` | 点缀色，如 electric blue、coral |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 卡片式 Card Layout | `Card-based dashboard UI, grid of uniform cards each containing icon title and stats, subtle drop shadows, rounded corners, light gray background, clean modern SaaS style` |
| 平面设计 · 面板磁贴 Dashboard Tiles | `Analytics dashboard with tile-based layout, row of KPI stat cards on top, charts and tables filling equal rectangular panels below, dark mode, data dense but legible` |
| 平面设计 · 模块化网格 Modular Grid | `Layout on a strict modular grid, equal square modules, content blocks snapping to grid, clean systematic arrangement, swiss design influence, plenty of white space` |
| 三维渲染 · 高透明钠钙玻璃 | `clear soda-lime glass, transparent, clean refractions, window glass` |
| 三维渲染 · 硼硅/铅晶质玻璃 | `crystal glass, cut glass, prismatic dispersion, fire, lead crystal` |
| 三维渲染 · 磨砂玻璃 | `frosted glass, ground glass, privacy glass, sandblasted, etched` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
