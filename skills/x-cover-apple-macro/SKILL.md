---
name: x-cover-apple-macro
description: X 长文封面图：苹果发布会微距（3D 微缩与商业产品质感）。黑天鹅绒底上的硬件微距特写，极致质感。 适用 AI 创作、AI 观察 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“苹果发布会微距”风格时使用。
---

# 苹果发布会微距

> 黑天鹅绒底上的硬件微距特写，极致质感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 创作、AI 观察 |
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

- **Identity 身份**：发布会级商业静物摄影
- **Spatial 空间**：左 1/3 微距主体，右侧大面积黑
- **Visual State 终端视觉状态**：[DEVICE] 微距特写，镜片镀膜泛紫，金属边缘锐利
- **Material 材质响应**：微喷砂钛金属，蓝宝石玻璃
- **Lighting 光学**：条形柔光箱掠射，锐利轮廓光

## 提示词模板

```text
Apple product keynote commercial photography, extreme macro close-up, pitch-black velvet background. Left third: precision studio shot of [DEVICE], pristine optical glass reflections, antireflective coatings, sharp metallic edge specular highlights. Right side generous dark negative space. Strip softbox rim lighting, ultra-photorealistic, medium format camera look, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[DEVICE]` | 硬件主体，如 a smartphone camera module in deep matte burgundy titanium、an AI chip die |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 三维渲染 · 产品级棚拍写实 + 无畸变正视或 3/4 视角 + 三点布光/高调纯白；材质如实还原 | `product visualization, studio render, hero shot, e-commerce, packaging` |
| 三维渲染 · 镜面抛光金属（铬/银） | `mirror chrome, polished silver, flawless reflections, high reflectivity` |
| 三维渲染 · 微距抽象 | `macro abstract, extreme close-up, surface texture study, microscopic details` |
| 三维渲染 · 边缘轮廓光 | `rim light, edge light, silhouette, kicker, backlight` |
| 三维渲染 · 无畸变产品正视 | `product front view, zero distortion, telecentric look, orthogonal shot` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
