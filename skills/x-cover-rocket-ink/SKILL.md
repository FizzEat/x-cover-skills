---
name: x-cover-rocket-ink
description: X 长文封面图：黑白漫画火箭升空（黑白版画与哲学隐喻）。海外第二名同款：火箭冲破浓烟。适合“新开始/突破惯性”。 适用 职场成长、做号变现 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“黑白漫画火箭升空”风格时使用。
---

# 黑白漫画火箭升空

> 海外第二名同款：火箭冲破浓烟。适合“新开始/突破惯性”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | C · 黑白版画与哲学隐喻 |
| 适用分类 | 职场成长、做号变现 |
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

- **Identity 身份**：挣脱引力的工业版画
- **Spatial 空间**：中景仰角，右侧发射塔，左下浓烟
- **Visual State 终端视觉状态**：火箭点火离地，滚滚白烟填满前景
- **Material 材质响应**：钢桁架硬质反光 vs 棉花状烟团
- **Lighting 光学**：尾焰为唯一主光源，逆光剪影

## 提示词模板

```text
Dramatic monochrome manga ink illustration, retro sci-fi space program style. A massive multistage [VEHICLE] lifting off from an intricate steel launch gantry at night, blinding white engine fire, monumental billowing clouds of smoke rolling across the foreground. Intricate cross-hatching line art, high dynamic range black and white, metaphor for breaking inertia, no text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[VEHICLE]` | 升空主体，如 Saturn V style rocket、a giant paper airplane（反差版） |

## 标题排版

- **中文区**：中文区使用时只加一行细衬线小标题，放在画面下方 1/5 的暗部，字号不超过画高 8%。
- **海外区**：不放字，或只放作者名小签名。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 少女漫画长线条 | `shojo manga flowing line style, long flowing multi-strand hair, slender limbs, ornate clustered eyelashes, fine hatching, CLAMP, Naoko Takeuchi` |
| 动画 · 圆润橡皮管（Rubber Hose） | `rubber hose animation style, jointless hose-like limbs, white gloves, pie eyes, 1920s-30s, Fleischer Studios, early Disney Mickey, bouncy walk cycle` |
| 三维渲染 · 黑白单色 | `black and white, monochrome, grayscale, noir, desaturate` |
| 三维渲染 · 硬光聚光灯+挡叶片 | `hard spotlight, barn doors, focused beam, cucoloris shadows, theatrical` |
| 动画 · 漫画网点化造型 | `manga screentone-styled design, halftone dot fills, hatching shadows, speed line backgrounds, speech balloons, onomatopoeia` |
| 动画 · 圆润卡通 | `round cartoon character design, sphere and cylinder geometric simplification, no sharp angles, friendly and cute, modern Disney TVA kids show` |

## 避坑

- 不要加彩色，不要加 UI 元素；隐喻只用一个，主体在画面里要足够小才有巨物感。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
