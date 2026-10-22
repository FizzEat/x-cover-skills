---
name: x-cover-before-after-income
description: X 长文封面图：收益战报对比（中文区强文字转化）。左边 0 右边 N 的战报式对比，数字后期叠加。 适用 做号变现、财经币圈 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“收益战报对比”风格时使用。
---

# 收益战报对比

> 左边 0 右边 N 的战报式对比，数字后期叠加。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | I · 中文区强文字转化 |
| 适用分类 | 做号变现、财经币圈 |
| 区域倾向 | 中文区优先 |
| 推荐画幅 | 16:9 出图，上传 X 长文前裁成 5:2，主体放中间 60% 安全区 |

## 工作流

1. 读用户给的长文标题、摘要或正文，提炼一句话核心观点和目标读者。
2. 把观点翻译成本风格能承载的画面：按下方“变量”逐个填空，变量必须是具体的可见物体，不写抽象词。
3. 输出 3 个版本：**稳妥版**（贴近模板）、**强钩子版**（放大冲突或尺度）、**反差版**（换一个意料之外的主体）。
4. 每个版本给出：中文画面说明一句 + 完整英文提示词 + 标题排版建议。
5. 按用户使用的模型补参数：Midjourney 末尾加 `--ar 16:9 --style raw`；FLUX / GPT-Image / Imagen 直接用自然语言并在开头写 `16:9 landscape`；即梦/豆包可把提示词翻成中文。
6. 提醒用户：画面里的文字一律后期排版，AI 只负责底图。

## PGVP 结构拆解

- **Identity 身份**：收益/成长战报底图
- **Spatial 空间**：左右二分，中间箭头
- **Visual State 终端视觉状态**：左侧空荡钱包或平线图，右侧上升图表与金币
- **Material 材质响应**：扁平 3D
- **Lighting 光学**：右侧更亮

## 提示词模板

```text
Two-panel banner, left panel shows [BEFORE] in dull gray, right panel shows [AFTER] in vibrant green and gold, a big bold arrow between them, empty label areas above each panel for numbers, clean flat 3D style, high contrast, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[BEFORE]` | 之前，如 an empty wallet and a flat line chart |
| `[AFTER]` | 之后，如 a rising chart with stacked gold coins |

## 标题排版

- **中文区**：主标题 ≤ 14 字，必须含数字或结果；副标题写人群或场景；视觉元素只做辅助证据。
- **海外区**：海外区不推荐此家族，如必须使用，把字量压到一半。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 全屏分屏 Split Screen | `Split screen landing page, left half photography mood image, right half solid color with headline and form, perfectly divided 50/50, modern clean, choice-oriented design` |
| 三维渲染 · 赛博朋克/抽象 + 任意风格镜头 + 霓虹自发光明暗对比 | `NFT artwork, 3D collectible, crypto art, digital art, 1/1` |
| 三维渲染 · 影视级写实 | `cinematic, photorealistic, Arri Alexa, film grain, shallow depth of field, color graded, film look` |
| 动画 · 高对比黑白木刻 | `high-contrast black-white woodcut texture, knife marks and wood grain, stark black and white, woodblock print, intaglio and relief` |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 平面设计 · Bodoni（现代衬线高对比） | `Vogue style magazine cover with Bodoni title, extreme contrast modern serif, supermodel portrait, glossy red lip, luxury fashion` |

## 避坑

- AI 生成的中文字不可直接用：先出无字底图（标注留白区），再用 Figma/稿定/Canva 排字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
