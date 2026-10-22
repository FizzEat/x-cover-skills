---
name: x-cover-ukiyoe-wave
description: X 长文封面图：浮世绘大浪（手绘插画与漫画叙事）。神奈川冲浪里式的大浪，隐喻“浪潮来了”。 适用 AI 观察、财经币圈、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“浮世绘大浪”风格时使用。
---

# 浮世绘大浪

> 神奈川冲浪里式的大浪，隐喻“浪潮来了”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | AI 观察、财经币圈、综合 |
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

- **Identity 身份**：浮世绘木版画
- **Spatial 空间**：巨浪占画面左 2/3，右侧小舟
- **Visual State 终端视觉状态**：巨浪由 [WAVE_MATTER] 构成，浪尖爪状，远处富士山
- **Material 材质响应**：和纸纹理，木版套色
- **Lighting 光学**：平涂，无透视光影

## 提示词模板

```text
Ukiyo-e woodblock print in the style of the great wave, a towering wave made of [WAVE_MATTER] curling over tiny boats, claw-like foam, distant Mount Fuji, Prussian blue and cream palette, washi paper texture, Edo period aesthetic, no text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[WAVE_MATTER]` | 浪的构成，如 binary code and data streams、gold coins |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 浮世绘版画风 | `ukiyo-e, Japanese woodblock print, flat color fields, contour lines, stylized waves, ukiyo` |
| 电影画面 · 日本静观长镜 | `Japanese contemplative long take, static camera, natural sound, empty frames, Ozu small actions` |
| 平面设计 · 版画质感 Print Texture（木刻/石版） | `woodcut style music festival poster, carved wood texture bold simplified figures, letterpress text, rustic handmade craft fair` |
| 摄影 · 日本战后写实主义/VIVO Postwar Japanese photography | `postwar Japanese photography 1950s, VIVO collective 1959, black and white, high contrast, medium grain, subjective documentary, Eikoh Hosoe Shomei Tomatsu, occupied Japan anxiety` |
| 动画 · 日本电视动画量产管线（虫制作体系） | `Japanese TV anime mass-production pipeline, Mushi Production system, limited animation on threes, static holds with camera moves, mouth loops, bank shot reuse` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
