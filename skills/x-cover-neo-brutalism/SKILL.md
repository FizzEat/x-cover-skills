---
name: x-cover-neo-brutalism
description: X 长文封面图：新粗野主义（极简编辑与书封海报）。粗黑描边、硬阴影、高饱和色块，网页风的叛逆感。 适用 做号变现、AI 编程、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“新粗野主义”风格时使用。
---

# 新粗野主义

> 粗黑描边、硬阴影、高饱和色块，网页风的叛逆感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | G · 极简编辑与书封海报 |
| 适用分类 | 做号变现、AI 编程、综合 |
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

- **Identity 身份**：新粗野主义网页风
- **Spatial 空间**：错落叠放的卡片
- **Visual State 终端视觉状态**：粗黑描边卡片和按钮，硬投影，[ELEMENTS]
- **Material 材质响应**：纯平色块
- **Lighting 光学**：无光，硬投影

## 提示词模板

```text
Neo-brutalism web design poster, thick black outlines, hard offset drop shadows, saturated flat colors (yellow, pink, mint), stacked cards and chunky buttons, [ELEMENTS], raw and playful, no gradients, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ELEMENTS]` | 元素，如 a cursor arrow, a star sticker, a big checkbox |

## 标题排版

- **中文区**：标题就是画面主角，使用宋体/思源宋体或粗黑体，字距收紧，严格对齐网格。
- **海外区**：大号衬线或 Grotesk 标题，配作者名和“Essay / Issue No.”等编辑元素。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 新粗野主义网页 Neo-Brutalism Web | `Neo-brutalist website landing page, default Times New Roman or Arial, chunky black outlines, high contrast clashing colors, hard drop shadows, brutal raw layout, anti-design, Gumroad style` |
| 平面设计 · 微软雅黑 Microsoft YaHei（Windows 默认网页黑体） | `微软雅黑 Chinese news website screenshot, clean readable web body text, portal homepage layout, red navigation bar` |
| 平面设计 · 网页布局 Web Layout（官网/落地页） | `modern SaaS website homepage screenshot, clean hero with headline subheadline CTA button, feature grid below, testimonials, light theme` |
| 平面设计 · 网页横幅/Banner Web Banner | `Google display banner ad set, leaderboard rectangle skyscraper sizes, promo message with CTA, animated gif or HTML5, e-commerce sale` |

## 避坑

- 让 AI 只出版式底图和图形元素，标题文字一定后期排，AI 排字会破坏网格。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
