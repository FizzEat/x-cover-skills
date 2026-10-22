---
name: x-cover-ink-sumi-zen
description: X 长文封面图：禅意水墨留白（黑白版画与哲学隐喻）。一笔水墨 + 大量留白，讲“少即是多/专注/断舍离”。 适用 职场成长、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“禅意水墨留白”风格时使用。
---

# 禅意水墨留白

> 一笔水墨 + 大量留白，讲“少即是多/专注/断舍离”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | C · 黑白版画与哲学隐喻 |
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

- **Identity 身份**：禅意水墨极简
- **Spatial 空间**：主体只占 15%，其余留白
- **Visual State 终端视觉状态**：[SUBJECT] 以寥寥数笔墨色画出，旁有一枚朱红印章
- **Material 材质响应**：宣纸纤维，墨色晕染
- **Lighting 光学**：无光影，纸白即光

## 提示词模板

```text
Zen sumi-e ink painting, extreme minimalism, [SUBJECT] painted in a few confident brush strokes, vast empty rice paper negative space, a small red seal stamp, ink bleeding into paper fibers, calm and meditative, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SUBJECT]` | 主体，如 a single enso circle、a lone fisherman on still water |

## 标题排版

- **中文区**：中文区使用时只加一行细衬线小标题，放在画面下方 1/5 的暗部，字号不超过画高 8%。
- **海外区**：不放字，或只放作者名小签名。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 水墨流动动画 | `ink wash flow animation, ink diffusing in water, rice-paper bleed, five ink tones, calligraphic negative space, Shanghai Film Studio` |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 动画 · 水墨浓淡晕染 | `ink wash tonal gradation, five ink tones burnt-thick-heavy-light-clear, rice-paper bleed, feibai flying-white, negative space, Shanghai Film Studio` |
| 动画 · 留白负空间 | `negative space emptiness, large empty or solid-color area, off-center small subject, Eastern minimalism, breathing room, copy space` |
| 平面设计 · 水墨飞白 Ink Wash & Brush Calligraphy | `chinese ink wash landscape painting, mountains in mist with bold brush strokes and blank space, traditional scroll aesthetic, zen calm` |

## 避坑

- 不要加彩色，不要加 UI 元素；隐喻只用一个，主体在画面里要足够小才有巨物感。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
