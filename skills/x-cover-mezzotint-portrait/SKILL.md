---
name: x-cover-mezzotint-portrait
description: X 长文封面图：美柔汀暗调肖像（黑白版画与哲学隐喻）。从黑暗里浮现的半张脸，适合人物志、心理、自我认知。 适用 职场成长、综合 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“美柔汀暗调肖像”风格时使用。
---

# 美柔汀暗调肖像

> 从黑暗里浮现的半张脸，适合人物志、心理、自我认知。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | C · 黑白版画与哲学隐喻 |
| 适用分类 | 职场成长、综合 |
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

- **Identity 身份**：美柔汀铜版暗调肖像
- **Spatial 空间**：人物侧脸占右半，左侧深黑
- **Visual State 终端视觉状态**：[PERSON] 侧脸从纯黑背景中渐显，只有轮廓被光勾出
- **Material 材质响应**：美柔汀天鹅绒般的黑与细腻灰阶
- **Lighting 光学**：单侧窄光，伦勃朗式

## 提示词模板

```text
Mezzotint print portrait, velvety deep blacks, [PERSON] in profile emerging from pure darkness, only the edge of the face caught by a narrow sliver of light, rich tonal gradation, old master printmaking, contemplative and introspective, large dark negative space on the left, no text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[PERSON]` | 人物，如 a thoughtful young founder、an old philosopher |

## 标题排版

- **中文区**：中文区使用时只加一行细衬线小标题，放在画面下方 1/5 的暗部，字号不超过画高 8%。
- **海外区**：不放字，或只放作者名小签名。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 伦勃朗光 | `rembrandt lighting, triangle light, dramatic portrait, painterly light` |
| 三维渲染 · 低调情绪暗场 | `dark moody, low key lighting, high contrast, chiaroscuro, dramatic shadows, film noir` |
| 平面设计 · 铜版纸 Coated Gloss Art Paper | `coated gloss art paper sample swatch book, shiny reflective sheets showing vivid CMYK prints, commercial printing paper selection` |
| 三维渲染 · 影视写实或三渲二 + 85mm 人像 + 三点布光/伦勃朗；皮肤 SSS、毛发 groom | `character render, portrait, realistic human, stylized character, hero` |
| 三维渲染 · 低调暗场 | `low key, dark mood, chiaroscuro, dramatic shadows, film noir` |
| 电影画面 · 伦勃朗三点布光 | `Rembrandt three-point lighting, triangle cheek light, classic portrait` |

## 避坑

- 不要加彩色，不要加 UI 元素；隐喻只用一个，主体在画面里要足够小才有巨物感。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
