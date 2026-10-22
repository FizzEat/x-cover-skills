---
name: x-cover-sketchnote-page
description: X 长文封面图：视觉笔记手账页（手绘插画与漫画叙事）。一页读书笔记式手账：标题框、气泡、小图、箭头，信息密而不乱。 适用 职场成长、AI 观察、做号变现 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“视觉笔记手账页”风格时使用。
---

# 视觉笔记手账页

> 一页读书笔记式手账：标题框、气泡、小图、箭头，信息密而不乱。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | 职场成长、AI 观察、做号变现 |
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

- **Identity 身份**：视觉笔记手账
- **Spatial 空间**：满版手账页面，中心主题框
- **Visual State 终端视觉状态**：中心 [TOPIC_ICON]，四周放射出 6 个笔记块
- **Material 材质响应**：点阵笔记本纸，彩色荧光笔
- **Lighting 光学**：俯拍平光，纸张轻微阴影

## 提示词模板

```text
Visual sketchnote page on dotted notebook paper, central hand-drawn [TOPIC_ICON] with 6 surrounding note clusters, banners, speech bubbles, doodle icons, arrows and highlighter strokes in yellow and teal, handwritten placeholder squiggles, overhead flat lay of a real notebook with a pen beside it, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[TOPIC_ICON]` | 中心主题图标，如 a light bulb brain |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 概念艺术手绘风 | `concept art style, painterly brushstrokes, digital painting, artstation, loose edges, matte painting` |
| 动画 · 粗野涂鸦 | `crude doodle style, shaky hand-drawn lines, unbalanced proportions, childlike doodle feel, Don Hertzfeldt stick figure, existential anxiety humor` |
| 动画 · 手绘赛璐璐 | `hand-painted cel animation on transparent celluloid, flat color fills, crisp outlines, vintage 1930s-90s cartoon, multiplane camera` |
| 平面设计 · 手绘涂鸦 Doodle & Hand-Drawn | `hand-drawn doodle arrows circles underlines on meeting notes, casual sketch annotations, whiteboard brainstorm vibe, approachable` |
| 动画 · 炭笔手绘动画 | `charcoal drawn animation, bold black charcoal lines, smudged grayscale, expressionist, high contrast black and white, William Kentridge erasure method` |
| 动画 · 吉卜力工作室全手绘体系 | `Studio Ghibli style, full hand-drawn animation, detailed natural phenomena, realistic proportion characters, thick watercolor backgrounds, Hayao Miyazaki, Isao Takahata, Kazuo Oga background art` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
