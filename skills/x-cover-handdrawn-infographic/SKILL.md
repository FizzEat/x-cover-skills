---
name: x-cover-handdrawn-infographic
description: X 长文封面图：米白纸手绘信息图（手绘插画与漫画叙事）。米白纸 + 墨黑线 + 单一强调色，克制的手绘知识卡（与“手绘信息图”skill 同源）。 适用 AI 观察、AI 编程、职场成长 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“米白纸手绘信息图”风格时使用。
---

# 米白纸手绘信息图

> 米白纸 + 墨黑线 + 单一强调色，克制的手绘知识卡（与“手绘信息图”skill 同源）。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | AI 观察、AI 编程、职场成长 |
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

- **Identity 身份**：手绘知识信息图
- **Spatial 空间**：标题横跨顶部，下方 3~4 个分区
- **Visual State 终端视觉状态**：墨线手绘 [ELEMENTS]，只有关键处用 [ACCENT] 一种颜色高亮
- **Material 材质响应**：米白素描纸，0.5mm 墨线
- **Lighting 光学**：无阴影

## 提示词模板

```text
Hand-drawn infographic on warm off-white sketch paper, crisp black ink linework only, one single accent color [ACCENT] used sparingly for highlights, sections containing [ELEMENTS], hand-lettered placeholder labels, arrows and brackets, generous whitespace, thoughtful editorial sketchnote, no gradients, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ELEMENTS]` | 分区内容，如 a brain, a gear, a rising arrow, a magnifying glass |
| `[ACCENT]` | 强调色，如 vermilion red、cobalt blue |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 概念艺术手绘风 | `concept art style, painterly brushstrokes, digital painting, artstation, loose edges, matte painting` |
| 动画 · 新闻信息图动画 | `news infographic animation, news data/process explainer, fast turnaround, 15-60 seconds, big key numbers, source footnote, vertical social-first` |
| 三维渲染 · 黑白单色 | `black and white, monochrome, grayscale, noir, desaturate` |
| 动画 · 手绘赛璐璐 | `hand-painted cel animation on transparent celluloid, flat color fills, crisp outlines, vintage 1930s-90s cartoon, multiplane camera` |
| 平面设计 · 信息图 Infographic | `vertical infographic about climate change facts, clear headline, icon-based statistics, timeline chart, sources at bottom, educational shareable` |
| 电影画面 · 冷蓝 · 月光单色染色版 | `monochrome blue moonlight, silver-blue highlights, steel blue, near monochromatic, ethereal night` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
