---
name: x-cover-report-cover-serif
description: X 长文封面图：卖方研报扉页（机构研报与数据可视化）。像高盛/大摩研报扉页：米白纸、衬线大标题、一张小图表。 适用 财经币圈、AI 观察 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“卖方研报扉页”风格时使用。
---

# 卖方研报扉页

> 像高盛/大摩研报扉页：米白纸、衬线大标题、一张小图表。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | B · 机构研报与数据可视化 |
| 适用分类 | 财经币圈、AI 观察 |
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

- **Identity 身份**：机构深度研报扉页封面
- **Spatial 空间**：左上大标题区，右下小图表，严谨网格
- **Visual State 终端视觉状态**：一张极简折线或面积图 [CHART] 与细线脚注
- **Material 材质响应**：米白哑光纸，墨蓝与橙色
- **Lighting 光学**：平面无光影

## 提示词模板

```text
Institutional equity research report cover page, off-white matte paper, generous margins, large empty serif title area top left, a small elegant [CHART] in navy and orange bottom right, hairline rules and footnote placeholders, restrained editorial finance aesthetic, print design, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[CHART]` | 图表类型，如 area chart of rising compute spend、line chart with a single annotation |

## 标题排版

- **中文区**：标题写结论而不是话题（“算力需求 5 年翻 30 倍”），核心数字单独放大。
- **海外区**：英文衬线大标题 + 一条橙色短破折号，模仿卖方研报扉页。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · Futura（几何无衬线经典） | `Futura typographic poster, geometric sans-serif uppercase, red circle and triangle motifs, Bauhaus influence, clean white background` |
| 平面设计 · Garamond / Adobe Garamond Pro（老式衬线标杆） | `Adobe Garamond Pro book interior page, old style serif body text, justified paragraphs, warm paper tone, fine literature typesetting` |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 平面设计 · 对称古典版心 Symmetric Classical Format | `Classical book page, symmetric centered type block, generous proportional margins, traditional serif typeface, formal balanced composition, fine press quality` |
| 平面设计 · Gill Sans（英伦人文无衬线） | `Gill Sans book cover design, British humanist sans-serif title, warm cream background, classic literary feel, understated elegance` |
| 平面设计 · Frutiger（导视人文无衬线） | `Frutiger airport wayfinding sign mockup, highly legible humanist sans-serif, directional arrows, blue white high contrast, calm authoritative` |

## 避坑

- 图表数字由 AI 生成大概率错，柱子和曲线只要形状，数字标签后期手动排。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
