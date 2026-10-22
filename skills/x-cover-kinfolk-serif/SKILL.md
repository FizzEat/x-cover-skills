---
name: x-cover-kinfolk-serif
description: X 长文封面图：Kinfolk 杂志极简（极简编辑与书封海报）。暖白底 + 一件小物 + 优雅衬线，生活方式杂志封面。 适用 职场成长、AI 创作、综合 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“Kinfolk 杂志极简”风格时使用。
---

# Kinfolk 杂志极简

> 暖白底 + 一件小物 + 优雅衬线，生活方式杂志封面。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | G · 极简编辑与书封海报 |
| 适用分类 | 职场成长、AI 创作、综合 |
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

- **Identity 身份**：生活方式杂志封面
- **Spatial 空间**：物件居中偏上，下方衬线标题
- **Visual State 终端视觉状态**：一件 [OBJECT] 安静地放在桌面，大量留白
- **Material 材质响应**：亚麻纸，自然材质
- **Lighting 光学**：北窗柔光

## 提示词模板

```text
Kinfolk magazine style cover, warm off-white background, a single [OBJECT] placed quietly on a linen surface, vast negative space, soft north window light, muted earthy palette, slow living aesthetic, elegant serif title area at the bottom, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[OBJECT]` | 物件，如 a ceramic cup and an open notebook |

## 标题排版

- **中文区**：标题就是画面主角，使用宋体/思源宋体或粗黑体，字距收紧，严格对齐网格。
- **海外区**：大号衬线或 Grotesk 标题，配作者名和“Essay / Issue No.”等编辑元素。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · Futura（几何无衬线经典） | `Futura typographic poster, geometric sans-serif uppercase, red circle and triangle motifs, Bauhaus influence, clean white background` |
| 平面设计 · 杂志跨页 Magazine Spread | `Luxury magazine double page spread, full-bleed hero image spanning both pages across gutter, kicker text top left, large serif headline, elegant fashion editorial look` |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 电影画面 · 自然光写实 | `natural available light, realistic daylight, no visible film lighting` |
| 平面设计 · Gill Sans（英伦人文无衬线） | `Gill Sans book cover design, British humanist sans-serif title, warm cream background, classic literary feel, understated elegance` |
| 平面设计 · Didot / HTF Didot（时尚杂志现代体） | `Didot perfume advertisement, French modern serif headline, minimalist glass bottle, marble background, high fashion editorial` |

## 避坑

- 让 AI 只出版式底图和图形元素，标题文字一定后期排，AI 排字会破坏网格。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
