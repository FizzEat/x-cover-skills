---
name: x-cover-endless-maze
description: X 长文封面图：无尽迷宫（超现实概念隐喻）。俯视迷宫中的人，讲“困局与出口”。 适用 职场成长、AI 观察 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“无尽迷宫”风格时使用。
---

# 无尽迷宫

> 俯视迷宫中的人，讲“困局与出口”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | K · 超现实概念隐喻 |
| 适用分类 | 职场成长、AI 观察 |
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

- **Identity 身份**：俯视迷宫隐喻
- **Spatial 空间**：正俯视，迷宫满版
- **Visual State 终端视觉状态**：巨大迷宫中一个 [FIGURE]，远处出口发光
- **Material 材质响应**：石墙或树篱
- **Lighting 光学**：斜光长影

## 提示词模板

```text
Top-down view of a vast intricate maze, a single tiny [FIGURE] in the middle, one glowing exit far away, long shadows from low sun, minimal palette, conceptual metaphor of finding a way out, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[FIGURE]` | 人物，如 a person in a red coat |

## 标题排版

- **中文区**：标题用一句反问或判断，压在画面最安静的区域。
- **海外区**：无字或极小标题，隐喻本身就是标题。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 高角度俯拍（渺小感） | `high angle looking down, small vulnerable figure, bird's eye feel` |
| 三维渲染 · 概念艺术手绘风 | `concept art style, painterly brushstrokes, digital painting, artstation, loose edges, matte painting` |
| 动画 · 俯拍上帝视角 | `overhead god's-eye view, straight down or above 60 degrees, characters small, environment dominates frame, omniscient perspective, layout showcase` |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 镜头角度 · 顶拍 / 垂直俯拍 Top shot / Overhead 90°（顶视） | `High Angle Shot` |
| 电影画面 · 八十年代高概念霓虹 | `1980s high concept neon, saturated pinks purples, haze machines, synthwave, stylish nightlife` |

## 避坑

- 一个画面只放一个反常识，叠加两个以上隐喻会让读者看不懂。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
