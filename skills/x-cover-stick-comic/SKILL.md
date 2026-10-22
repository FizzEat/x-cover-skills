---
name: x-cover-stick-comic
description: X 长文封面图：火柴人极简漫画（手绘插画与漫画叙事）。xkcd 式火柴人 + 一句讽刺，程序员与互联网人秒懂。 适用 职场成长、AI 编程、综合 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“火柴人极简漫画”风格时使用。
---

# 火柴人极简漫画

> xkcd 式火柴人 + 一句讽刺，程序员与互联网人秒懂。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | 职场成长、AI 编程、综合 |
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

- **Identity 身份**：极简火柴人讽刺漫画
- **Spatial 空间**：单格或三格横排
- **Visual State 终端视觉状态**：火柴人在 [SITUATION]，表情用最少线条
- **Material 材质响应**：纯白底黑色签字笔线
- **Lighting 光学**：无光影

## 提示词模板

```text
Minimalist stick figure webcomic, black pen lines on pure white, [SITUATION], expressive with minimal lines, three-panel horizontal layout, nerdy deadpan humor, empty speech bubbles for later text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SITUATION]` | 情境，如 staring at a bug at 3am while an AI agent fixes it instantly |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 少女漫画长线条 | `shojo manga flowing line style, long flowing multi-strand hair, slender limbs, ornate clustered eyelashes, fine hatching, CLAMP, Naoko Takeuchi` |
| 三维渲染 · 极简主义 | `minimalist, clean composition, negative space, monochrome palette, simple geometry` |
| 动画 · 漫画网点化造型 | `manga screentone-styled design, halftone dot fills, hatching shadows, speed line backgrounds, speech balloons, onomatopoeia` |
| 三维渲染 · 极简/几何抽象 + 等距正交 + 高调纯色；循环无缝动画 | `motion graphics, looping animation, geometric shapes, mg, broadcast` |
| 三维渲染 · 等距小场景/极简 + 正交相机 + 单柔光箱；圆润倒角柔和投影 | `3D icon, isometric icon, UI icon, app glyph, cute 3D` |
| 三维渲染 · 极简/粘土 + 正交正视 + 单侧柔光；识别度高、少细节 | `app icon, 3D glyph, cute 3D icon, simple, app store` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
