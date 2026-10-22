---
name: x-cover-excalidraw-doodle
description: X 长文封面图：Excalidraw 粉彩涂鸦流程（手绘插画与漫画叙事）。零基础教程神器：手绘粉彩小图标 + 箭头流程，视觉门槛极低。 适用 AI 编程、AI 创作、做号变现 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“Excalidraw 粉彩涂鸦流程”风格时使用。
---

# Excalidraw 粉彩涂鸦流程

> 零基础教程神器：手绘粉彩小图标 + 箭头流程，视觉门槛极低。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | AI 编程、AI 创作、做号变现 |
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

- **Identity 身份**：白板手绘教学插画
- **Spatial 空间**：左侧标题，右侧横向环形工作流
- **Visual State 终端视觉状态**：[STEPS] 手绘小图标由箭头串联，最后回到一台笑脸笔记本
- **Material 材质响应**：毡尖笔与粉彩马克笔，糙面卡纸
- **Lighting 光学**：无阴影平面

## 提示词模板

```text
Cute pastel tech workflow doodle, Excalidraw and Notion style explainer illustration, clean cream paper background. Left side reserved for handwritten bold header with a warm orange marker underline. Right side: a step-by-step horizontal pipeline of charming hand-drawn pastel icons: [STEPS], connected by sketchy arrows, looping back to a smiling laptop. Soft felt-tip outlines, mint, coral, lemon and baby blue highlights, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[STEPS]` | 4~5 个步骤图标，如 1. document stack, 2. cleaning broom, 3. smiling robot, 4. bar chart, 5. cloud upload |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 概念艺术手绘风 | `concept art style, painterly brushstrokes, digital painting, artstation, loose edges, matte painting` |
| 动画 · 粗野涂鸦 | `crude doodle style, shaky hand-drawn lines, unbalanced proportions, childlike doodle feel, Don Hertzfeldt stick figure, existential anxiety humor` |
| 平面设计 · 有限色扁平插画调色盘 Limited Flat Palette | `flat illustration set with limited 5-color palette, isometric office scenes, clean vector, SaaS onboarding illustrations, consistent branding` |
| 动画 · 手绘赛璐璐 | `hand-painted cel animation on transparent celluloid, flat color fills, crisp outlines, vintage 1930s-90s cartoon, multiplane camera` |
| 平面设计 · 手绘涂鸦 Doodle & Hand-Drawn | `hand-drawn doodle arrows circles underlines on meeting notes, casual sketch annotations, whiteboard brainstorm vibe, approachable` |
| 动画 · 炭笔手绘动画 | `charcoal drawn animation, bold black charcoal lines, smudged grayscale, expressionist, high contrast black and white, William Kentridge erasure method` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
