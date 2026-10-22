---
name: x-cover-japanese-ma
description: X 长文封面图：日式留白（間）（极简编辑与书封海报）。无印良品式的安静：一条线、一个点、大量空白。 适用 职场成长、AI 创作、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“日式留白（間）”风格时使用。
---

# 日式留白（間）

> 无印良品式的安静：一条线、一个点、大量空白。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | G · 极简编辑与书封海报 |
| 适用分类 | 职场成长、AI 创作、综合 |
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

- **Identity 身份**：日式极简“间”
- **Spatial 空间**：主体极小，偏离中心
- **Visual State 终端视觉状态**：一个 [OBJECT] 位于画面三分点，其余空白
- **Material 材质响应**：和纸或水泥
- **Lighting 光学**：柔和散射光

## 提示词模板

```text
Japanese minimalist design with ma (negative space), a single small [OBJECT] placed at a third point, vast calm empty space, washi paper texture, soft diffused light, muted natural tones, quiet and refined, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[OBJECT]` | 物件，如 a stone、a branch、a tiny red dot |

## 标题排版

- **中文区**：标题就是画面主角，使用宋体/思源宋体或粗黑体，字距收紧，严格对齐网格。
- **海外区**：大号衬线或 Grotesk 标题，配作者名和“Essay / Issue No.”等编辑元素。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 电影画面 · 日本静观长镜 | `Japanese contemplative long take, static camera, natural sound, empty frames, Ozu small actions` |
| 三维渲染 · 极简主义 | `minimalist, clean composition, negative space, monochrome palette, simple geometry` |
| 动画 · 留白负空间 | `negative space emptiness, large empty or solid-color area, off-center small subject, Eastern minimalism, breathing room, copy space` |
| 摄影 · 日本战后写实主义/VIVO Postwar Japanese photography | `postwar Japanese photography 1950s, VIVO collective 1959, black and white, high contrast, medium grain, subjective documentary, Eikoh Hosoe Shomei Tomatsu, occupied Japan anxiety` |

## 避坑

- 让 AI 只出版式底图和图形元素，标题文字一定后期排，AI 排字会破坏网格。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
