---
name: x-cover-iceberg
description: X 长文封面图：冰山模型（超现实概念隐喻）。水面上一小角，水下巨大，讲“你看不到的部分”。 适用 AI 观察、做号变现、职场成长 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“冰山模型”风格时使用。
---

# 冰山模型

> 水面上一小角，水下巨大，讲“你看不到的部分”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | K · 超现实概念隐喻 |
| 适用分类 | AI 观察、做号变现、职场成长 |
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

- **Identity 身份**：冰山剖面
- **Spatial 空间**：水平线在上 1/4
- **Visual State 终端视觉状态**：水上小尖，水下巨大冰体，水下有 [HIDDEN]
- **Material 材质响应**：通透冰与深蓝海水
- **Lighting 光学**：水面光线向下散射

## 提示词模板

```text
Iceberg cross-section illustration, small tip above the waterline, massive hidden body below, [HIDDEN] embedded inside the underwater ice, deep blue gradient ocean, light rays filtering down, clean editorial 3D style, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[HIDDEN]` | 水下隐藏物，如 gears, data, servers and people working |

## 标题排版

- **中文区**：标题用一句反问或判断，压在画面最安静的区域。
- **海外区**：无字或极小标题，隐喻本身就是标题。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 影视级写实 | `cinematic, photorealistic, Arri Alexa, film grain, shallow depth of field, color graded, film look` |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 三维渲染 · 卡通渲染 | `cel shaded, toon shader, flat colors, bold outlines, stepped shadows, cartoon` |
| 三维渲染 · 三渲二 | `anime style, cel animation, Studio Ghibli aesthetic, expressive line art, manga` |
| 三维渲染 · 粘土渲染 | `clay render, matte white clay, untextured, soft shadows, form study, mockup` |
| 三维渲染 · 等距小场景 | `isometric view, orthographic camera, tiny world, diorama, 2:1 pixel ratio, cute` |

## 避坑

- 一个画面只放一个反常识，叠加两个以上隐喻会让读者看不懂。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
