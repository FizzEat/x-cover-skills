---
name: x-cover-portal-door
description: X 长文封面图：旷野中的门（超现实概念隐喻）。荒野里一扇发光的门，通往另一个世界——“新机会”。 适用 职场成长、AI 观察、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“旷野中的门”风格时使用。
---

# 旷野中的门

> 荒野里一扇发光的门，通往另一个世界——“新机会”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | K · 超现实概念隐喻 |
| 适用分类 | 职场成长、AI 观察、综合 |
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

- **Identity 身份**：超现实门户
- **Spatial 空间**：门居中，地平线低
- **Visual State 终端视觉状态**：旷野里一扇打开的门，门内是 [OTHER_WORLD]，一个人站在门前
- **Material 材质响应**：真实材质
- **Lighting 光学**：门内光溢出

## 提示词模板

```text
Surreal landscape, a lone open door standing in an empty [LANDSCAPE], through the door a glimpse of [OTHER_WORLD] spilling light onto the ground, a person standing before it, cinematic, conceptual, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[LANDSCAPE]` | 旷野，如 desert、snowfield |
| `[OTHER_WORLD]` | 门内世界，如 a lush green spring、a neon city |

## 标题排版

- **中文区**：标题用一句反问或判断，压在画面最安静的区域。
- **海外区**：无字或极小标题，隐喻本身就是标题。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 超现实梦幻 | `surreal, dreamlike, floating objects, impossible scale, soft focus, ethereal, fantasy` |
| 摄影 · 新生儿摄影 Newborn photography | `newborn photography, sleeping baby, posed, soft pastel colors, f/2.8, warm studio light, softbox, wrapped blanket, tiny details, clean background, high key, gentle skin tones, props, safe posing, portrait, innocent` |
| 三维渲染 · 概念艺术手绘风 | `concept art style, painterly brushstrokes, digital painting, artstation, loose edges, matte painting` |
| 三维渲染 · 暗光生物发光 | `bioluminescent, dark environment, self-illuminated organs, translucent glow, deep sea, abyss` |
| 三维渲染 · 超现实/抽象 + 方形构图 + 特殊胶片 LUT；艺术感强 | `album cover, music artwork, surreal 3D, vinyl cover art` |
| 摄影 · 裸体艺术 Nude art photography | `fine art nude, human body, black and white, soft lighting, f/5.6, graceful pose, shadows and form, medium format, classical, tasteful, gallery art, skin texture, dramatic light, silhouette, timeless, sculptural` |

## 避坑

- 一个画面只放一个反常识，叠加两个以上隐喻会让读者看不懂。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
