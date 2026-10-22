---
name: x-cover-big-claim-poster
description: X 长文封面图：大字报痛点封面底（中文区强文字转化）。中文区主力：大字占 50%，右侧一个证据物件。AI 出底图，字后期排。 适用 做号变现、账号支付、AI 编程 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“大字报痛点封面底”风格时使用。
---

# 大字报痛点封面底

> 中文区主力：大字占 50%，右侧一个证据物件。AI 出底图，字后期排。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | I · 中文区强文字转化 |
| 适用分类 | 做号变现、账号支付、AI 编程 |
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

- **Identity 身份**：强文字转化封面底图
- **Spatial 空间**：左 55% 纯色留白（排大字），右侧证据物件
- **Visual State 终端视觉状态**：右侧一个 [PROOF] 3D 物件，带一点光效
- **Material 材质响应**：纯色或轻纹理底，3D 物件
- **Lighting 光学**：主体轮廓光

## 提示词模板

```text
Clean bold banner background, left 55% solid [BG] color area completely empty for large headline text, right side a single striking 3D [PROOF] with a subtle glow, high contrast, modern Chinese social media cover style, minimal decoration, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[BG]` | 底色，如 deep navy、bright yellow、black |
| `[PROOF]` | 证据物件，如 a stack of gold coins、a shield with a checkmark、a laptop |

## 标题排版

- **中文区**：主标题 ≤ 14 字，必须含数字或结果；副标题写人群或场景；视觉元素只做辅助证据。
- **海外区**：海外区不推荐此家族，如必须使用，把字量压到一半。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 三维渲染 · 高调纯净 | `high key, bright and airy, clean, minimal shadows, medical tech, sterile` |
| 三维渲染 · 影视级写实 | `cinematic, photorealistic, Arri Alexa, film grain, shallow depth of field, color graded, film look` |
| 三维渲染 · 高调纯白 | `high key, pure white cyclorama, clean studio, bright` |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 三维渲染 · 产品级棚拍写实 + 无畸变正视或 3/4 视角 + 三点布光/高调纯白；材质如实还原 | `product visualization, studio render, hero shot, e-commerce, packaging` |

## 避坑

- AI 生成的中文字不可直接用：先出无字底图（标注留白区），再用 Figma/稿定/Canva 排字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
