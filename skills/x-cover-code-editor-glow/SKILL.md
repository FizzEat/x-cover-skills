---
name: x-cover-code-editor-glow
description: X 长文封面图：代码编辑器光晕（工科蓝图与信息结构）。一块漂浮的编辑器窗口 + 品牌渐变光晕，像开发工具官网首屏。 适用 AI 编程 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“代码编辑器光晕”风格时使用。
---

# 代码编辑器光晕

> 一块漂浮的编辑器窗口 + 品牌渐变光晕，像开发工具官网首屏。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | AI 编程 |
| 区域倾向 | 海外区优先 |
| 推荐画幅 | 16:9 出图，上传 X 长文前裁成 5:2，主体放中间 60% 安全区 |

## 工作流

1. 读用户给的长文标题、摘要或正文，提炼一句话核心观点和目标读者。
2. 把观点翻译成本风格能承载的画面：按下方“变量”逐个填空，变量必须是具体的可见物体，不写抽象词。
3. 输出 3 个版本：**稳妥版**（贴近模板）、**强钩子版**（放大冲突或尺度）、**反差版**（换一个意料之外的主体）。
4. 每个版本给出：中文画面说明一句 + 完整英文提示词 + 标题排版建议。
5. 按用户使用的模型补参数：Midjourney 末尾加 `--ar 16:9 --style raw`；FLUX / GPT-Image / Imagen 直接用自然语言并在开头写 `16:9 landscape`；即梦/豆包可把提示词翻成中文。
6. 提醒用户：画面里的文字一律后期排版，AI 只负责底图。

## PGVP 结构拆解

- **Identity 身份**：开发者工具产品首屏封面
- **Spatial 空间**：编辑器窗口居中偏右，大角度透视
- **Visual State 终端视觉状态**：编辑器里是代码纹理和 AI 补全的高亮幽灵文本，背后 [GLOW] 渐变光晕
- **Material 材质响应**：玻璃窗口，柔和噪点渐变
- **Lighting 光学**：背光光晕 + 边缘高光

## 提示词模板

```text
Floating code editor window in dramatic 3D perspective, syntax highlighted code as abstract texture, an AI inline suggestion highlighted in ghost text, behind it a soft [GLOW] gradient aura with fine grain noise, dark background, glassmorphism window frame, premium developer tool landing page hero, clean negative space on the left, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[GLOW]` | 光晕配色，如 violet to orange、teal to blue |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 渐变背景灯 | `gradient background, colored backdrop, studio gradient, color wash` |
| 三维渲染 · 颗粒叠加 | `film grain, ISO 800, analog texture, fine grain, movie stock` |
| 动画 · UI 动效微交互 | `UI micro-interaction motion, button states loading transitions gesture hints, 150-400ms easing curve, clear semantics, low-power Lottie SVG vector` |
| 三维渲染 · 程序化抽象 + 实验镜头 + 霓虹/渐变背景；高饱和强节奏 | `abstract 3D art, procedural forms, colorful, generative, modern art` |
| 电影画面 · 35mm · 500T夜景推冲粗颗粒 | `pushed 500T night, heavy film grain, gritty shadows, nocturnal` |
| 平面设计 · Segoe UI / Open Sans / Lato（UI 三件套） | `Segoe UI Windows application window mockup, clean interface typography, light theme, readable form labels, native desktop app` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
