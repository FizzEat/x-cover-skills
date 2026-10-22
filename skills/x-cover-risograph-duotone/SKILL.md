---
name: x-cover-risograph-duotone
description: X 长文封面图：Riso 孔版双色（黑白版画与哲学隐喻）。孔版印刷的套色错位与颗粒，独立杂志感，年轻又有态度。 适用 做号变现、AI 创作、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“Riso 孔版双色”风格时使用。
---

# Riso 孔版双色

> 孔版印刷的套色错位与颗粒，独立杂志感，年轻又有态度。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | C · 黑白版画与哲学隐喻 |
| 适用分类 | 做号变现、AI 创作、综合 |
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

- **Identity 身份**：独立出版物孔版印刷
- **Spatial 空间**：主体大块剪影，几何辅助形
- **Visual State 终端视觉状态**：[SUBJECT] 以两色叠印，套色轻微错位
- **Material 材质响应**：Riso 颗粒，荧光色油墨
- **Lighting 光学**：平面无光影

## 提示词模板

```text
Risograph print illustration, two-color overprint in [COLORS], slight misregistration, grainy ink texture, [SUBJECT] as bold flat shapes, halftone gradients, indie zine aesthetic, off-white paper, playful and edgy, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[COLORS]` | 两种油墨色，如 fluorescent pink and blue、orange and teal |
| `[SUBJECT]` | 主体 |

## 标题排版

- **中文区**：中文区使用时只加一行细衬线小标题，放在画面下方 1/5 的暗部，字号不超过画高 8%。
- **海外区**：不放字，或只放作者名小签名。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 孔版/理想印刷 Risograph | `risograph art poster, grainy soy ink layers, slight color misregistration, limited palette, handmade zine aesthetic` |
| 平面设计 · 低保真拼贴 Lo-fi Collage / Zine | `DIY punk zine cover, photocopied grain texture, scotch tape holding cut-out images, torn paper edges, hand-drawn marker arrows and circles, risograph two-color misregister, raw` |
| 平面设计 · 杂志跨页 Magazine Spread | `Luxury magazine double page spread, full-bleed hero image spanning both pages across gutter, kicker text top left, large serif headline, elegant fashion editorial look` |
| 动画 · 漫画网点化造型 | `manga screentone-styled design, halftone dot fills, hatching shadows, speed line backgrounds, speech balloons, onomatopoeia` |
| 平面设计 · 杂志 Magazine Editorial | `luxury fashion magazine spread, full-bleed image across gutter, large serif headline, layered captions, editorial typography` |
| 动画 · 网点半调 | `screentone halftone texture, printed halftone dots, manga print feel, rosette moire pattern, pop art` |

## 避坑

- 不要加彩色，不要加 UI 元素；隐喻只用一个，主体在画面里要足够小才有巨物感。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
