---
name: x-cover-halftone-noir
description: X 长文封面图：网点黑色电影（黑白版画与哲学隐喻）。放大的半调网点 + 黑色电影剪影，冷峻有张力。 适用 职场成长、AI 观察、综合 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“网点黑色电影”风格时使用。
---

# 网点黑色电影

> 放大的半调网点 + 黑色电影剪影，冷峻有张力。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | C · 黑白版画与哲学隐喻 |
| 适用分类 | 职场成长、AI 观察、综合 |
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

- **Identity 身份**：网点印刷黑色电影
- **Spatial 空间**：剪影人物占一侧，大面积网点渐变
- **Visual State 终端视觉状态**：[SCENE] 的剪影，百叶窗光线穿过，网点颗粒放大可见
- **Material 材质响应**：粗网点印刷，报纸纸纹
- **Lighting 光学**：硬光侧打，强阴影

## 提示词模板

```text
Film noir halftone illustration, enlarged coarse halftone dots visible, [SCENE] in stark silhouette, venetian blind light stripes across the wall, hard side lighting, deep shadows, black and white with a single [ACCENT] spot color, vintage pulp print texture, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SCENE]` | 剪影场景，如 a man in a trench coat staring at a glowing monitor |
| `[ACCENT]` | 唯一点缀色，如 red、none |

## 标题排版

- **中文区**：中文区使用时只加一行细衬线小标题，放在画面下方 1/5 的暗部，字号不超过画高 8%。
- **海外区**：不放字，或只放作者名小签名。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 漫画网点化造型 | `manga screentone-styled design, halftone dot fills, hatching shadows, speed line backgrounds, speech balloons, onomatopoeia` |
| 电影画面 · 黑色电影（Film Noir, 1940s–50s） | `1940s film noir, high contrast black and white, venetian blind shadows, rain slick streets, cynical detective` |
| 三维渲染 · 硬光聚光灯+挡叶片 | `hard spotlight, barn doors, focused beam, cucoloris shadows, theatrical` |
| 三维渲染 · 低调情绪暗场 | `dark moody, low key lighting, high contrast, chiaroscuro, dramatic shadows, film noir` |
| 动画 · 网点半调 | `screentone halftone texture, printed halftone dots, manga print feel, rosette moire pattern, pop art` |
| 平面设计 · 黑色电影霓虹 Noir Neon | `noir neon alley scene poster, deep black shadows with glowing pink and cyan neon signs, wet pavement reflections, rain night, cinematic` |

## 避坑

- 不要加彩色，不要加 UI 元素；隐喻只用一个，主体在画面里要足够小才有巨物感。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
