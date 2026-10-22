---
name: x-cover-heatmap-grid
description: X 长文封面图：热力图矩阵（机构研报与数据可视化）。一整面热力格子，颜色本身就是结论（哪里热、哪里冷）。 适用 财经币圈、AI 观察 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“热力图矩阵”风格时使用。
---

# 热力图矩阵

> 一整面热力格子，颜色本身就是结论（哪里热、哪里冷）。

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

- **Identity 身份**：市场/行业热力分布封面
- **Spatial 空间**：满版方格矩阵，少量格子突出
- **Visual State 终端视觉状态**：数百个方格按 [PALETTE] 渐变着色，少数格子发光凸起
- **Material 材质响应**：平面矢量，细白缝隙
- **Lighting 光学**：凸起格子自发光

## 提示词模板

```text
Full-bleed treemap heatmap of hundreds of rectangular tiles colored in a [PALETTE] gradient, a few tiles extruded in 3D and glowing to show outliers, thin white gaps between tiles, clean data art, institutional market map aesthetic, dark background, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[PALETTE]` | 配色，如 red-to-green market colors、blue-to-orange diverging |

## 标题排版

- **中文区**：标题写结论而不是话题（“算力需求 5 年翻 30 倍”），核心数字单独放大。
- **海外区**：英文衬线大标题 + 一条橙色短破折号，模仿卖方研报扉页。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · CAD 原生数据导入 | `CAD import, STEP file, IGES, parasolid, industrial design` |
| 平面设计 · 模块化网格 Modular Grid | `Layout on a strict modular grid, equal square modules, content blocks snapping to grid, clean systematic arrangement, swiss design influence, plenty of white space` |
| 摄影 · Leica Summilux-M 50mm f/1.4 ASPH（2004 版，8 片 5 组，含非球面 + 浮动，Leica 官网数据） | `Leica Summilux-M 50mm f/1.4 ASPH, 8 elements, Leica M, creamy melting bokeh, warm skin tones, subtle spherical glow, 3D pop, sharp at f/2, Leica M6, Kodak Portra 800, low light street, f/1.4, shallow depth of field` |
| 摄影 · Leica Noctilux-M 75mm f/1.25 ASPH（9 片 6 组，2 非球面，Leica 官网数据） | `Leica Noctilux-M 75mm f/1.25 ASPH, portrait lens, flattering 75mm compression, warm skin tones, hazy glow wide open, extremely melting bokeh, sharp at f/2, Leica M, Pro 400H, f/1.4, golden hour, romantic portrait` |
| 动画 · 数据可视化动态图表 | `data visualization motion chart, data changes over time, bar chart race line flow heatmap, synchronized value labels, traceable source data` |
| 平面设计 · 数据报表/年报 Data Report & Annual Report | `corporate annual report open spread, CEO letter, financial highlights infographics, sustainability data charts, clean ESG reporting design` |

## 避坑

- 图表数字由 AI 生成大概率错，柱子和曲线只要形状，数字标签后期手动排。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
