---
name: x-cover-knolling-flatlay
description: X 长文封面图：Knolling 平铺整理（3D 微缩与商业产品质感）。工具整齐 90 度排列俯拍，最适合“工具清单/装备推荐”。 适用 AI 编程、做号变现、AI 创作 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“Knolling 平铺整理”风格时使用。
---

# Knolling 平铺整理

> 工具整齐 90 度排列俯拍，最适合“工具清单/装备推荐”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 编程、做号变现、AI 创作 |
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

- **Identity 身份**：Knolling 俯拍平铺
- **Spatial 空间**：正俯视，网格对齐
- **Visual State 终端视觉状态**：[ITEMS] 按 90 度整齐排列，彼此等距
- **Material 材质响应**：实物材质，哑光桌面
- **Lighting 光学**：柔和顶光，极浅阴影

## 提示词模板

```text
Knolling flat lay photography, perfectly organized [ITEMS] arranged at 90 degree angles with equal spacing on a [SURFACE], top-down view, soft overhead light, minimal shadows, satisfying order, clean product catalog aesthetic, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ITEMS]` | 物品，如 laptop, keyboard, phone, notebook, coffee, headphones |
| `[SURFACE]` | 桌面，如 matte sand-colored table |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 高角度俯拍（渺小感） | `high angle looking down, small vulnerable figure, bird's eye feel` |
| 镜头角度 · 顶视/平铺/flat lay | `Flat lay, overhead, top-down, 90-degree` |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 三维渲染 · 极简主义 | `minimalist, clean composition, negative space, monochrome palette, simple geometry` |
| 动画 · 俯拍上帝视角 | `overhead god's-eye view, straight down or above 60 degrees, characters small, environment dominates frame, omniscient perspective, layout showcase` |
| 三维渲染 · 无畸变产品正视 | `product front view, zero distortion, telecentric look, orthogonal shot` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
