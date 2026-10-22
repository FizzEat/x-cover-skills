---
name: x-cover-scratchboard
description: X 长文封面图：刮板画高光雕刻（黑白版画与哲学隐喻）。黑底刮出白线，像钞票雕刻一样精密，适合金融与权力主题。 适用 AI 观察、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“刮板画高光雕刻”风格时使用。
---

# 刮板画高光雕刻

> 黑底刮出白线，像钞票雕刻一样精密，适合金融与权力主题。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | C · 黑白版画与哲学隐喻 |
| 适用分类 | AI 观察、综合 |
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

- **Identity 身份**：刮板画/钞票雕刻风
- **Spatial 空间**：主体居中对称，环形纹饰
- **Visual State 终端视觉状态**：[SUBJECT] 由密集白色刮线塑形，周围钞票式扭索纹
- **Material 材质响应**：黑色刮板，锐利白线
- **Lighting 光学**：线条本身即光

## 提示词模板

```text
Scratchboard illustration, white lines scratched from black surface, [SUBJECT] rendered in dense precise engraving lines like banknote intaglio, ornamental guilloche patterns framing it, symmetrical composition, crisp and authoritative, no text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SUBJECT]` | 主体，如 a robot head in profile、a bull and bear |

## 标题排版

- **中文区**：中文区使用时只加一行细衬线小标题，放在画面下方 1/5 的暗部，字号不超过画高 8%。
- **海外区**：不放字，或只放作者名小签名。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 浮世绘版画风 | `ukiyo-e, Japanese woodblock print, flat color fields, contour lines, stylized waves, ukiyo` |
| 平面设计 · 纹样与底纹 Patterns & Textures | `seamless geometric pattern texture, four-directional repeat, brand decorative motif, wrapping paper or fabric print application --tile` |
| 三维渲染 · 黑白单色 | `black and white, monochrome, grayscale, noir, desaturate` |
| 电影画面 · 中心对称构图（韦斯·安德森式） | `centered symmetrical composition, Wes Anderson style, mirror balance, dead center` |
| 平面设计 · 版画质感 Print Texture（木刻/石版） | `woodcut style music festival poster, carved wood texture bold simplified figures, letterpress text, rustic handmade craft fair` |
| 电影画面 · 黑白高反差（Noir High Contrast） | `black and white high contrast noir, crushed blacks, hard bright highlights, dramatic shadows, film grain` |

## 避坑

- 不要加彩色，不要加 UI 元素；隐喻只用一个，主体在画面里要足够小才有巨物感。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
