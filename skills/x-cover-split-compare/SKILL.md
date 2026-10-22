---
name: x-cover-split-compare
description: X 长文封面图：左右对比 Before/After（工科蓝图与信息结构）。左边混乱右边整洁，一眼看懂“用了这个方法之后”。 适用 AI 编程、AI 创作、职场成长 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“左右对比 Before/After”风格时使用。
---

# 左右对比 Before/After

> 左边混乱右边整洁，一眼看懂“用了这个方法之后”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | AI 编程、AI 创作、职场成长 |
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

- **Identity 身份**：前后对比转化封面
- **Spatial 空间**：对角或垂直二分，左暗右亮
- **Visual State 终端视觉状态**：左侧 [BEFORE]，右侧 [AFTER]，中间一个大箭头或分割光带
- **Material 材质响应**：左侧粗糙杂乱纹理，右侧干净玻璃与白色
- **Lighting 光学**：左冷暗、右暖亮的色温对比

## 提示词模板

```text
Split screen before and after comparison banner. Left half: [BEFORE], desaturated, cold dim lighting, messy. Right half: [AFTER], bright, clean, organized, warm light. A bold glowing arrow or light beam divides the two halves. High contrast storytelling, clean modern 3D illustration style, clear focal points on each side, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[BEFORE]` | 改变前的状态，如 a chaotic desk buried in sticky notes and error windows |
| `[AFTER]` | 改变后，如 a calm minimal desk with one glowing dashboard |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 全屏分屏 Split Screen | `Split screen landing page, left half photography mood image, right half solid color with headline and form, perfectly divided 50/50, modern clean, choice-oriented design` |
| 平面设计 · 对角分割 Diagonal Split | `Sports poster with bold diagonal split dividing two color fields, athlete silhouette on one side, big slanted typography on the other, high contrast neon, aggressive energy` |
| 三维渲染 · 高调纯净 | `high key, bright and airy, clean, minimal shadows, medical tech, sterile` |
| 三维渲染 · 低调情绪暗场 | `dark moody, low key lighting, high contrast, chiaroscuro, dramatic shadows, film noir` |
| 三维渲染 · 高调纯白 | `high key, pure white cyclorama, clean studio, bright` |
| 三维渲染 · 低调暗场 | `low key, dark mood, chiaroscuro, dramatic shadows, film noir` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
