---
name: x-cover-swiss-infographic
description: X 长文封面图：瑞士网格信息图（工科蓝图与信息结构）。严格网格 + 大号编号 + 色块，读起来像一份设计精良的报告。 适用 AI 观察、财经币圈、职场成长 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“瑞士网格信息图”风格时使用。
---

# 瑞士网格信息图

> 严格网格 + 大号编号 + 色块，读起来像一份设计精良的报告。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | AI 观察、财经币圈、职场成长 |
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

- **Identity 身份**：瑞士国际主义信息图封面
- **Spatial 空间**：12 栏网格，左上大号数字编号，右侧 3 行模块
- **Visual State 终端视觉状态**：大号编号 01/02/03 与几何色块、细分割线、箭头图示 [DIAGRAM]
- **Material 材质响应**：平面印刷感，无纹理纯色
- **Lighting 光学**：无光影的纯平面

## 提示词模板

```text
Swiss International Style infographic poster, strict modular grid, oversized numerals 01 02 03 in Helvetica-like grotesk, bold geometric color blocks in red, black and off-white, thin hairline dividers, small arrow diagrams showing [DIAGRAM], asymmetric layout with lots of white space, flat print design, no gradients, no shadows, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[DIAGRAM]` | 图示内容，如 three stages of AI adoption、input-process-output |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 瑞士国际主义 Swiss International Style | `Swiss Style poster design, mathematical grid layout, asymmetric balance, Helvetica typography flush left, objective black and white photography, generous white space, minimal` |
| 平面设计 · 瑞士朋克 Swiss Punk / 新浪潮 | `Swiss Punk typographic poster, Wolfgang Weingart style, multiple overlapping layers of mixed weight sans-serif type, ruled lines crossing, letterpress texture, chaotic rhythm, cyan magenta misregistration` |
| 平面设计 · 模块化网格 Modular Grid | `Layout on a strict modular grid, equal square modules, content blocks snapping to grid, clean systematic arrangement, swiss design influence, plenty of white space` |
| 平面设计 · 栏式网格 Column Grid | `Editorial magazine page, six-column grid, body text flowing in columns, wide gutters, pull quotes spanning two columns, clean serif typography, structured` |
| 平面设计 · 极简瑞士回潮 Neo-Swiss Minimal | `Neo-Swiss minimalist poster, single Helvetica family only, extreme asymmetric grid, huge white margins, one small bold element, restrained monochrome with one accent color, gallery aesthetic` |
| 平面设计 · 瑞士新浪潮 Swiss New Wave | `Swiss New Wave poster by April Greiman, transparent overlapping layers, pixelated and vector mixed, photography with colored overlays, tilted perspective typography, early digital glitch, blue magenta` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
