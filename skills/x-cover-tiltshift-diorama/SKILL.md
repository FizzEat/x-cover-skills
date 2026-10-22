---
name: x-cover-tiltshift-diorama
description: X 长文封面图：移轴微缩模型（3D 微缩与商业产品质感）。小人偶 + 发光方块，把抽象概念做成桌面微缩剧场。 适用 职场成长、做号变现、AI 观察 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“移轴微缩模型”风格时使用。
---

# 移轴微缩模型

> 小人偶 + 发光方块，把抽象概念做成桌面微缩剧场。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | 职场成长、做号变现、AI 观察 |
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

- **Identity 身份**：概念微缩场景摄影
- **Spatial 空间**：桌面低视角，浅景深
- **Visual State 终端视觉状态**：微缩小人 [ACTION]，连接一个发光的 [OBJECT]
- **Material 材质响应**：树脂手办质感，半透明发光体
- **Lighting 光学**：柔和侧光，背景虚化

## 提示词模板

```text
Conceptual miniature diorama photography, tilt-shift macro lens, warm clean beige tabletop background. A tiny scale figurine [ACTION], connected by a single cable to a glowing [OBJECT]. Soft directional studio light, subsurface scattering, delicate contact shadows, shallow depth of field, whimsical yet sophisticated editorial metaphor, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ACTION]` | 小人在做什么，如 in work clothes holding a laptop |
| `[OBJECT]` | 发光物，如 emerald green frosted glass cube |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 移轴微缩 | `tilt shift, miniature faking, selective focus plane, toy town` |
| 三维渲染 · 拟真微缩模型 | `tilt shift, miniature faking, diorama, toy photography, macro selective focus` |
| 三维渲染 · 微距抽象 | `macro abstract, extreme close-up, surface texture study, microscopic details` |
| 三维渲染 · 浅景深微距 | `macro 100mm f/2.8, extreme close-up, shallow depth of field, focus plane` |
| 电影画面 · 移轴/倾斜焦平面（Tilt-Shift） | `tilt-shift selective focus, diagonal plane of focus, miniature effect` |
| 三维渲染 · 高调纯净/极简 + 微距 + 蝴蝶光/夹光；玻璃霜瓶、水珠 | `beauty product, cosmetics render, skincare bottle, water droplets` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
