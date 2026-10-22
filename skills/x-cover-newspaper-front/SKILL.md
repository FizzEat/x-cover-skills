---
name: x-cover-newspaper-front
description: X 长文封面图：报纸头版号外（机构研报与数据可视化）。做成一份报纸头版，“号外”感天然有新闻价值。 适用 AI 观察、财经币圈、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“报纸头版号外”风格时使用。
---

# 报纸头版号外

> 做成一份报纸头版，“号外”感天然有新闻价值。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | B · 机构研报与数据可视化 |
| 适用分类 | AI 观察、财经币圈、综合 |
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

- **Identity 身份**：新闻头版号外封面
- **Spatial 空间**：报头横跨顶部，下方大标题区 + 主图
- **Visual State 终端视觉状态**：泛黄报纸，主图为 [PHOTO]，栏线与小字纹理
- **Material 材质响应**：新闻纸纤维纹理，油墨轻微晕开
- **Lighting 光学**：平光，轻微纸张折痕阴影

## 提示词模板

```text
Vintage newspaper front page extra edition, broadsheet masthead across the top, huge empty headline area, a halftone black and white news photo of [PHOTO], dense column text as texture, newsprint paper grain, slight ink bleed, folded crease, historic breaking-news mood, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[PHOTO]` | 头版照片，如 a crowd staring at a giant screen、a robot shaking hands with a CEO |

## 标题排版

- **中文区**：标题写结论而不是话题（“算力需求 5 年翻 30 倍”），核心数字单独放大。
- **海外区**：英文衬线大标题 + 一条橙色短破折号，模仿卖方研报扉页。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 漫画网点化造型 | `manga screentone-styled design, halftone dot fills, hatching shadows, speed line backgrounds, speech balloons, onomatopoeia` |
| 平面设计 · 双色专色印刷 Duotone Spot Color | `duotone music album cover, black and fluorescent pink halftone photo, bold spot color, indie record sleeve` |
| 平面设计 · Times New Roman（报纸标准过渡体） | `Times New Roman newspaper front page layout, dense column text, traditional masthead, grayscale photojournalism, classic broadsheet` |
| 平面设计 · 杂志跨页 Magazine Spread | `Luxury magazine double page spread, full-bleed hero image spanning both pages across gutter, kicker text top left, large serif headline, elegant fashion editorial look` |
| 动画 · 网点半调 | `screentone halftone texture, printed halftone dots, manga print feel, rosette moire pattern, pop art` |
| 平面设计 · 胶印 Offset Lithography | `CMYK offset printing press sheet, color registration marks and crop bars, four color halftone dots magnified, commercial print shop` |

## 避坑

- 图表数字由 AI 生成大概率错，柱子和曲线只要形状，数字标签后期手动排。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
