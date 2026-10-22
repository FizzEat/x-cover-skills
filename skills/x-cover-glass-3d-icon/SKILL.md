---
name: x-cover-glass-3d-icon
description: X 长文封面图：玻璃拟态 3D 图标（3D 微缩与商业产品质感）。一个晶莹的 3D 玻璃图标居中漂浮，新产品/新功能发布首选。 适用 AI 编程、AI 创作、AI 观察 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“玻璃拟态 3D 图标”风格时使用。
---

# 玻璃拟态 3D 图标

> 一个晶莹的 3D 玻璃图标居中漂浮，新产品/新功能发布首选。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 编程、AI 创作、AI 观察 |
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

- **Identity 身份**：玻璃拟态产品图标
- **Spatial 空间**：居中，周围大量渐变留白
- **Visual State 终端视觉状态**：[ICON_SHAPE] 形状的厚玻璃图标漂浮，内部有折射光
- **Material 材质响应**：厚磨砂玻璃，色散彩虹边
- **Lighting 光学**：柔和背光 + 焦散

## 提示词模板

```text
A single thick frosted glass 3D icon shaped like [ICON_SHAPE] floating in the center, internal refraction, chromatic dispersion rainbow edges, caustic light on the floor, soft [BG] gradient background, premium product launch aesthetic, octane render, minimal, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ICON_SHAPE]` | 图标形状，如 a sparkle star、a speech bubble、a cursor arrow |
| `[BG]` | 背景渐变色 |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 高透明钠钙玻璃 | `clear soda-lime glass, transparent, clean refractions, window glass` |
| 三维渲染 · 产品级写实 + 微距 + 多柔光箱/AOI 摄影棚；金属高抛、宝石焦散 | `jewelry render, watch macro, diamond caustics, gold polished, luxury` |
| 电影画面 · 游泳池池底折射光斑 | `pool caustics caustic light patterns, water ripple projection on face, summer cool` |
| 三维渲染 · 影视级写实 | `cinematic, photorealistic, Arri Alexa, film grain, shallow depth of field, color graded, film look` |
| 平面设计 · 内文版式 Book Interior Typesetting | `novel book interior spread, classic serif body text justified, chapter opener with drop cap, elegant margins` |
| 三维渲染 · 硼硅/铅晶质玻璃 | `crystal glass, cut glass, prismatic dispersion, fire, lead crystal` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
