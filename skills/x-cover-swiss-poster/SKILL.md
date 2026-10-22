---
name: x-cover-swiss-poster
description: X 长文封面图：瑞士海报（极简编辑与书封海报）。巨大字体与几何色块构成的瑞士海报，理性有力。 适用 AI 观察、AI 编程、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“瑞士海报”风格时使用。
---

# 瑞士海报

> 巨大字体与几何色块构成的瑞士海报，理性有力。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | G · 极简编辑与书封海报 |
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

- **Identity 身份**：瑞士国际主义海报
- **Spatial 空间**：不对称网格，大号字体主导
- **Visual State 终端视觉状态**：几何 [SHAPES] 与粗体字母块交错
- **Material 材质响应**：平面印刷，纯色
- **Lighting 光学**：无光影

## 提示词模板

```text
Swiss style poster, asymmetric grid, huge bold grotesk letterforms as graphic elements, geometric [SHAPES] in red black and white, precise alignment, flat print, rational and powerful, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SHAPES]` | 几何形，如 circles and diagonal bars |

## 标题排版

- **中文区**：标题就是画面主角，使用宋体/思源宋体或粗黑体，字距收紧，严格对齐网格。
- **海外区**：大号衬线或 Grotesk 标题，配作者名和“Essay / Issue No.”等编辑元素。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 瑞士国际主义 Swiss International Style | `Swiss Style poster design, mathematical grid layout, asymmetric balance, Helvetica typography flush left, objective black and white photography, generous white space, minimal` |
| 平面设计 · Helvetica Neue / Neue Haas Grotesk（新 grotesque 标杆） | `Helvetica Neue typography poster, clean neutral sans-serif, grid layout, black on white, Swiss Style minimalism, corporate identity` |
| 平面设计 · Akzidenz-Grotesk（瑞士风格源头） | `Akzidenz-Grotesk poster 1950s style, slightly irregular grotesque sans, muted vintage palette, offset print texture, mid-century modern` |
| 平面设计 · 模块化网格 Modular Grid | `Layout on a strict modular grid, equal square modules, content blocks snapping to grid, clean systematic arrangement, swiss design influence, plenty of white space` |
| 平面设计 · Nimbus Sans（Helvetica 度量兼容替代品） | `Nimbus Sans document typesetting, clean report page, metric compatible with Helvetica, professional typeset body text, gray and black` |
| 平面设计 · 栏式网格 Column Grid | `Editorial magazine page, six-column grid, body text flowing in columns, wide gutters, pull quotes spanning two columns, clean serif typography, structured` |

## 避坑

- 让 AI 只出版式底图和图形元素，标题文字一定后期排，AI 排字会破坏网格。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
