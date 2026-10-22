---
name: x-cover-roadmap-timeline
description: X 长文封面图：路线图时间轴（工科蓝图与信息结构）。一条蜿蜒道路串起里程碑，适合“30 天/从 0 到 1/学习路径”。 适用 职场成长、AI 编程、做号变现 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“路线图时间轴”风格时使用。
---

# 路线图时间轴

> 一条蜿蜒道路串起里程碑，适合“30 天/从 0 到 1/学习路径”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | 职场成长、AI 编程、做号变现 |
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

- **Identity 身份**：学习路线图封面
- **Spatial 空间**：S 形路径从左下延伸到右上，3~5 个里程碑
- **Visual State 终端视觉状态**：道路上依次立着 [MILESTONES]，终点有一面旗帜或发光奖杯
- **Material 材质响应**：低多边形或扁平 3D 质感，柔和色块
- **Lighting 光学**：清晨暖光，长阴影

## 提示词模板

```text
Isometric roadmap illustration, a winding S-shaped path rising from bottom left to top right across a soft pastel landscape, [COUNT] milestone markers along the road: [MILESTONES], a glowing flag at the summit, tiny figure walking on the path, clean flat 3D style, soft long shadows, left side open space for headline, optimistic learning-journey mood, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[COUNT]` | 里程碑数量 |
| `[MILESTONES]` | 每个里程碑的物件，如 a book, a laptop, a rocket, a trophy |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 时间轴 Timeline | `Vertical timeline infographic, central line with circular milestone nodes, alternate left-right content cards, date labels, clean flat vector style, corporate history` |
| 三维渲染 · 低多边形 | `low poly, flat shading, visible triangles, minimal design, vibrant color palette` |
| 动画 · 低多边形（Low-Poly） | `low-polygon design, visible triangular facets, origami-like flat planes, retro 3D PS1 era, flat shaded no smoothing` |
| 平面设计 · 低多边形 Low Poly | `low poly abstract animal head wallpaper, geometric triangular facets in gradient blues, polygonal deer wolf fox, modern tech background` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
