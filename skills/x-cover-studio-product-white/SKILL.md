---
name: x-cover-studio-product-white
description: X 长文封面图：白底产品棚拍（摄影与电影剧照）。纯白无缝背景的产品照，电商感和“清单感”。 适用 AI 创作、做号变现、账号支付 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“白底产品棚拍”风格时使用。
---

# 白底产品棚拍

> 纯白无缝背景的产品照，电商感和“清单感”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | H · 摄影与电影剧照 |
| 适用分类 | AI 创作、做号变现、账号支付 |
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

- **Identity 身份**：白底产品摄影
- **Spatial 空间**：主体居中，充足留白
- **Visual State 终端视觉状态**：[PRODUCT] 精准对焦，干净反射
- **Material 材质响应**：主体真实材质
- **Lighting 光学**：大柔光箱 + 顶光

## 提示词模板

```text
Studio product photography on pure white seamless background, [PRODUCT] in sharp focus, clean reflections, large softbox and top light, soft contact shadow, commercial catalog quality, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[PRODUCT]` | 产品，如 a smartphone and a SIM card、a physical credit card mockup without numbers |

## 标题排版

- **中文区**：选主体偏一侧的画面，在暗部或天空放白字，必要时加 20% 黑色渐变压暗。
- **海外区**：无字或电影海报式底部小字。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 三维渲染 · 产品级棚拍写实 + 无畸变正视或 3/4 视角 + 三点布光/高调纯白；材质如实还原 | `product visualization, studio render, hero shot, e-commerce, packaging` |
| 三维渲染 · 高调纯净 | `high key, bright and airy, clean, minimal shadows, medical tech, sterile` |
| 三维渲染 · 卡通/粘土 + 正交 + 白底/描边；PNG 透明底 | `3D sticker, social media sticker, transparent background, emoji 3D` |
| 三维渲染 · 无畸变产品正视 | `product front view, zero distortion, telecentric look, orthogonal shot` |
| 三维渲染 · 产品级棚拍 + 无畸变正视 + 高调纯白/渐变背景；无干扰物 | `e-commerce hero image, amazon main image, white background product` |

## 避坑

- 避免网红滤镜和过度磨皮；人物不要直视镜头摆拍，抓拍感更像真实故事。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
