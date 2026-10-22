---
name: x-cover-papercraft-layers
description: X 长文封面图：纸艺层叠（3D 微缩与商业产品质感）。多层剪纸叠出纵深，手作温度 + 立体感。 适用 AI 创作、职场成长、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“纸艺层叠”风格时使用。
---

# 纸艺层叠

> 多层剪纸叠出纵深，手作温度 + 立体感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 创作、职场成长、综合 |
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

- **Identity 身份**：多层剪纸立体插画
- **Spatial 空间**：层层向内的纵深隧道或景观
- **Visual State 终端视觉状态**：[SCENE] 由多层彩色卡纸剪出，层间有阴影
- **Material 材质响应**：卡纸纤维，裁切边缘
- **Lighting 光学**：侧光造出层间阴影

## 提示词模板

```text
Layered paper cut art, multiple layers of colored cardstock creating depth, [SCENE], visible paper fibers and cut edges, soft shadows between layers, side lighting, handcrafted diorama, harmonious [PALETTE] palette, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SCENE]` | 场景，如 a tunnel leading to a bright idea bulb |
| `[PALETTE]` | 配色 |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 纸雕剪纸风 | `paper craft, paper cutout, layered paper, soft contact shadows, handmade, kirigami` |
| 三维渲染 · 影视写实/写实游戏风 + 广角 + 日光+体积雾；大气透视层次 | `environment design, landscape, epic scenery, atmospheric fog, vista` |
| 动画 · 剪纸动画 | `paper cut-out stop-motion, articulated paper puppets, visible rivet joints, hard edges, paper fiber texture, folk art style` |
| 动画 · 多层玻璃台复合（剪纸＋景深） | `multiplane glass-table paper cut-out animation, layered depth of field, parallax movement, glass surface reflection, Lotte Reiniger silhouette, multiplane camera` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
