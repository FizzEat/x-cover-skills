---
name: x-cover-woodcut-bold
description: X 长文封面图：粗犷木刻版画（黑白版画与哲学隐喻）。刀痕粗犷的木刻，力量感强，适合“劳动/坚持/手艺”主题。 适用 职场成长、综合、做号变现 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“粗犷木刻版画”风格时使用。
---

# 粗犷木刻版画

> 刀痕粗犷的木刻，力量感强，适合“劳动/坚持/手艺”主题。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | C · 黑白版画与哲学隐喻 |
| 适用分类 | 职场成长、综合、做号变现 |
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

- **Identity 身份**：表现主义木刻版画
- **Spatial 空间**：主体占画面中心大块面
- **Visual State 终端视觉状态**：[SUBJECT] 以粗刀痕刻出，背景放射状刀纹
- **Material 材质响应**：木纹肌理，黑墨不均匀转印
- **Lighting 光学**：高对比，无中间调

## 提示词模板

```text
Bold expressionist woodcut print, thick gouged knife marks, raw black ink on cream rice paper with visible wood grain texture, [SUBJECT] carved in heavy blocky shapes, radiating gouge lines in the background, uneven ink transfer, powerful high contrast, no midtones, no text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SUBJECT]` | 主体，如 a blacksmith hammering a glowing chip、a farmer planting seeds made of code |

## 标题排版

- **中文区**：中文区使用时只加一行细衬线小标题，放在画面下方 1/5 的暗部，字号不超过画高 8%。
- **海外区**：不放字，或只放作者名小签名。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 高对比黑白木刻 | `high-contrast black-white woodcut texture, knife marks and wood grain, stark black and white, woodblock print, intaglio and relief` |
| 三维渲染 · 浮世绘版画风 | `ukiyo-e, Japanese woodblock print, flat color fields, contour lines, stylized waves, ukiyo` |
| 三维渲染 · 黑白单色 | `black and white, monochrome, grayscale, noir, desaturate` |
| 动画 · 油画肌理刮刀 | `oil paint palette-knife texture, heavy impasto knife marks, paint strings,刮刀 scratching white ground, Van Gogh animated style` |
| 平面设计 · 版画质感 Print Texture（木刻/石版） | `woodcut style music festival poster, carved wood texture bold simplified figures, letterpress text, rustic handmade craft fair` |
| 电影画面 · 黑白高反差（Noir High Contrast） | `black and white high contrast noir, crushed blacks, hard bright highlights, dramatic shadows, film grain` |

## 避坑

- 不要加彩色，不要加 UI 元素；隐喻只用一个，主体在画面里要足够小才有巨物感。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
