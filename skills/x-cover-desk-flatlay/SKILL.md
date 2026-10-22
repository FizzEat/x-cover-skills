---
name: x-cover-desk-flatlay
description: X 长文封面图：工作台俯拍（摄影与电影剧照）。真实桌面俯拍：电脑、咖啡、笔记，“我是怎么工作的”。 适用 AI 编程、做号变现、职场成长 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“工作台俯拍”风格时使用。
---

# 工作台俯拍

> 真实桌面俯拍：电脑、咖啡、笔记，“我是怎么工作的”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | H · 摄影与电影剧照 |
| 适用分类 | AI 编程、做号变现、职场成长 |
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

- **Identity 身份**：真实工作台俯拍
- **Spatial 空间**：俯拍，屏幕位于画面一侧
- **Visual State 终端视觉状态**：桌面上 [ITEMS]，屏幕亮着显示 [SCREEN]
- **Material 材质响应**：木桌、陶瓷、纸张真实质感
- **Lighting 光学**：侧窗自然光

## 提示词模板

```text
Top-down photo of a real workspace desk, [ITEMS], laptop screen showing [SCREEN] as blurred UI, morning side window light, natural shadows, authentic and lived-in, editorial lifestyle photography, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ITEMS]` | 桌面物品，如 coffee, notebook, phone, glasses |
| `[SCREEN]` | 屏幕内容，如 a chat with an AI assistant |

## 标题排版

- **中文区**：选主体偏一侧的画面，在暗部或天空放白字，必要时加 20% 黑色渐变压暗。
- **海外区**：无字或电影海报式底部小字。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 高角度俯拍（渺小感） | `high angle looking down, small vulnerable figure, bird's eye feel` |
| 电影画面 · 自然光写实 | `natural available light, realistic daylight, no visible film lighting` |
| 镜头角度 · 生活方式/使用场景 | `In-context / lifestyle` |
| 动画 · 俯拍上帝视角 | `overhead god's-eye view, straight down or above 60 degrees, characters small, environment dominates frame, omniscient perspective, layout showcase` |
| 电影画面 · 达内兄弟手持自然光纪实 | `Dardenne brothers handheld natural light, following behind shoulder, social realism, working class` |
| 镜头角度 · 顶拍 / 垂直俯拍 Top shot / Overhead 90°（顶视） | `High Angle Shot` |

## 避坑

- 避免网红滤镜和过度磨皮；人物不要直视镜头摆拍，抓拍感更像真实故事。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
