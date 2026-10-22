---
name: x-cover-penguin-classic
description: X 长文封面图：经典平装书封（极简编辑与书封海报）。三段式经典平装书封，让一篇长文像一本必读书。 适用 职场成长、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“经典平装书封”风格时使用。
---

# 经典平装书封

> 三段式经典平装书封，让一篇长文像一本必读书。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | G · 极简编辑与书封海报 |
| 适用分类 | 职场成长、综合 |
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

- **Identity 身份**：经典平装书封面
- **Spatial 空间**：上中下三段色带，中间白底标题
- **Visual State 终端视觉状态**：顶部和底部 [COLOR] 色带，中间白色标题区，小徽标
- **Material 材质响应**：旧书纸张，略磨损
- **Lighting 光学**：平面

## 提示词模板

```text
Classic mid-century paperback book cover, horizontal tri-band layout, [COLOR] bands at top and bottom, cream central band reserved for title, small round emblem, worn paper texture, timeless literary design, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[COLOR]` | 色带颜色，如 orange (fiction)、green (crime)、blue (non-fiction) |

## 标题排版

- **中文区**：标题就是画面主角，使用宋体/思源宋体或粗黑体，字距收紧，严格对齐网格。
- **海外区**：大号衬线或 Grotesk 标题，配作者名和“Essay / Issue No.”等编辑元素。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · Caslon / Sabon（传统书籍正文衬线） | `Caslon classic novel title page, traditional old style serif, centered imprints, cream laid paper, letterpress impression` |
| 三维渲染 · 九十年代早期 CG 复古 | `90s CGI, retro computer graphics, PS1 era, Gouraud shading, low res textures, VHS` |
| 平面设计 · 对称古典版心 Symmetric Classical Format | `Classical book page, symmetric centered type block, generous proportional margins, traditional serif typeface, formal balanced composition, fine press quality` |
| 平面设计 · Plantin / Bulmer（过渡时期书籍体） | `Plantin hardcover novel dust jacket, transitional serif subtitle, textured cloth binding, restrained color blocking, literary fiction` |
| 电影画面 · 复古褪色（Vintage Fade） | `vintage faded film, lifted blacks, milky highlights, aged color shift, film dust scratches` |
| 平面设计 · 书籍封面 Book Cover | `book cover mockup on wooden shelf, bold title author name visible from far, atmospheric genre art, series branding consistent` |

## 避坑

- 让 AI 只出版式底图和图形元素，标题文字一定后期排，AI 排字会破坏网格。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
