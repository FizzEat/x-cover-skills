---
name: x-cover-qa-bubbles
description: X 长文封面图：问答对话气泡（中文区强文字转化）。左问右答的聊天气泡，适合“答疑/真相/你问我答”。 适用 AI 观察、职场成长、做号变现 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“问答对话气泡”风格时使用。
---

# 问答对话气泡

> 左问右答的聊天气泡，适合“答疑/真相/你问我答”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | I · 中文区强文字转化 |
| 适用分类 | AI 观察、职场成长、做号变现 |
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

- **Identity 身份**：问答对话底图
- **Spatial 空间**：左右交错的大对话气泡
- **Visual State 终端视觉状态**：左侧灰色问号气泡，右侧 [COLOR] 回答气泡，带头像占位
- **Material 材质响应**：UI 气泡，柔和阴影
- **Lighting 光学**：平面

## 提示词模板

```text
Chat conversation layout banner, large speech bubbles alternating left and right, left gray bubble with a big question mark, right [COLOR] bubble with an answer placeholder, small avatar circles, clean messaging UI aesthetic, soft shadows, empty bubble space for text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[COLOR]` | 回答气泡颜色 |

## 标题排版

- **中文区**：主标题 ≤ 14 字，必须含数字或结果；副标题写人群或场景；视觉元素只做辅助证据。
- **海外区**：海外区不推荐此家族，如必须使用，把字量压到一半。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · UI 动效微交互 | `UI micro-interaction motion, button states loading transitions gesture hints, 150-400ms easing curve, clear semantics, low-power Lottie SVG vector` |
| 平面设计 · 卡片式 Card Layout | `Card-based dashboard UI, grid of uniform cards each containing icon title and stats, subtle drop shadows, rounded corners, light gray background, clean modern SaaS style` |
| 平面设计 · Segoe UI / Open Sans / Lato（UI 三件套） | `Segoe UI Windows application window mockup, clean interface typography, light theme, readable form labels, native desktop app` |
| 平面设计 · 移动界面 Mobile App UI | `iOS mobile banking app screens set, tab bar navigation, card lists, biometric login, clean modern fintech interface` |
| 平面设计 · 动态图形 Motion Graphics Title/UI | `motion graphics title sequence for tech keynote, kinetic typography revealing key message, smooth easing, subtle particle background, broadcast quality` |
| 平面设计 · 液体金属 Liquid Metal & Chrome | `liquid chrome abstract 3D shape on pastel gradient background, reflective metallic balloon form, Y2K futuristic poster` |

## 避坑

- AI 生成的中文字不可直接用：先出无字底图（标注留白区），再用 Figma/稿定/Canva 排字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
