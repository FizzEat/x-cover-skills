---
name: x-cover-brick-build
description: X 长文封面图：积木搭建（3D 微缩与商业产品质感）。塑料积木一块块搭出系统，隐喻“模块化/搭建”。 适用 AI 编程、做号变现、职场成长 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“积木搭建”风格时使用。
---

# 积木搭建

> 塑料积木一块块搭出系统，隐喻“模块化/搭建”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 编程、做号变现、职场成长 |
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

- **Identity 身份**：塑料积木搭建场景
- **Spatial 空间**：中景，搭建中的结构
- **Visual State 终端视觉状态**：积木小人正在搭建 [STRUCTURE]，散落零件
- **Material 材质响应**：光滑 ABS 塑料，凸点
- **Lighting 光学**：明亮棚拍，浅景深

## 提示词模板

```text
Toy plastic building bricks, a half-built [STRUCTURE] with minifigure-style builders placing pieces, scattered bricks on a bright table, glossy ABS plastic with studs, shallow depth of field, playful macro photography, no brand logos, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[STRUCTURE]` | 搭建对象，如 a robot、a data pipeline with conveyor belts |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 微距抽象 | `macro abstract, extreme close-up, surface texture study, microscopic details` |
| 三维渲染 · 哑光塑料（ABS/PP） | `matte plastic, soft touch coating, non-reflective, ABS` |
| 三维渲染 · 浅景深微距 | `macro 100mm f/2.8, extreme close-up, shallow depth of field, focus plane` |
| 三维渲染 · 高调纯净/极简 + 微距 + 蝴蝶光/夹光；玻璃霜瓶、水珠 | `beauty product, cosmetics render, skincare bottle, water droplets` |
| 三维渲染 · 亮面塑料（ABS/亚克力） | `glossy ABS plastic, shiny toy surface, acrylic, injection molding` |
| 三维渲染 · 景深合成 | `focus stack, all-in-focus macro, composite sharpness, depth blend` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
