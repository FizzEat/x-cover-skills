---
name: x-cover-retro-space-age
description: X 长文封面图：复古太空时代海报（宇宙科幻与未来视觉）。50~60 年代 NASA 风格海报，乐观的未来主义。 适用 AI 观察、AI 编程、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“复古太空时代海报”风格时使用。
---

# 复古太空时代海报

> 50~60 年代 NASA 风格海报，乐观的未来主义。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | D · 宇宙科幻与未来视觉 |
| 适用分类 | AI 观察、AI 编程、综合 |
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

- **Identity 身份**：复古未来主义海报
- **Spatial 空间**：主体居中，星空与行星环绕
- **Visual State 终端视觉状态**：[SUBJECT] 飞向巨大行星，复古宇航风格
- **Material 材质响应**：丝网印刷颗粒，有限色板
- **Lighting 光学**：平面渐变，星光

## 提示词模板

```text
Retro 1960s space age travel poster, screen print texture, limited palette of teal, orange and cream, [SUBJECT] soaring toward a giant ringed planet, stylized stars, mid-century modern illustration, optimistic retrofuturism, large empty band at top for title, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SUBJECT]` | 主体，如 a sleek rocket、a robot astronaut |

## 标题排版

- **中文区**：标题放在暗部天空区域，白色粗黑体，一句判断句。
- **海外区**：少字，大写无衬线短语（如 THE ENDGAME）。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 九十年代早期 CG 复古 | `90s CGI, retro computer graphics, PS1 era, Gouraud shading, low res textures, VHS` |
| 平面设计 · 未来主义 Futurism | `Futurist typographic poster, words in freedom scattered across canvas, explosive onomatopoeia text of various sizes, diagonal movement, machinery noise, multiple perspectives simultaneously, aggressive` |
| 平面设计 · 丝网印刷 Screen Printing | `serigraphy screen print poster, thick vibrant ink layers, halftone dot texture, hand-pulled prints, gig poster aesthetic` |
| 平面设计 · 装饰艺术运动 Art Deco | `Art Deco poster 1920s, sunburst rays background, zigzag geometric border, gold foil accents, stylized fountain figure, elegant tall sans serif, luxurious, symmetrical` |
| 电影画面 · 复古褪色（Vintage Fade） | `vintage faded film, lifted blacks, milky highlights, aged color shift, film dust scratches` |
| 电影画面 · 复古镜头低反差眩光 | `vintage lens low contrast flare, hazy backlight, washed-out colors, retro` |

## 避坑

- 避免廉价的蓝紫光污染和满屏粒子，保留大面积暗部给标题。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
