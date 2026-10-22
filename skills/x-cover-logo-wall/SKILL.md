---
name: x-cover-logo-wall
description: X 长文封面图：工具矩阵 Logo 墙（中文区强文字转化）。“N 个工具全测评”：整齐的 App 图标网格，中间一个高亮。 适用 AI 编程、AI 创作、做号变现 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“工具矩阵 Logo 墙”风格时使用。
---

# 工具矩阵 Logo 墙

> “N 个工具全测评”：整齐的 App 图标网格，中间一个高亮。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | I · 中文区强文字转化 |
| 适用分类 | AI 编程、AI 创作、做号变现 |
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

- **Identity 身份**：工具合集图标墙
- **Spatial 空间**：满版网格，中心一个放大
- **Visual State 终端视觉状态**：数十个泛化圆角 App 图标网格，中央 [HERO] 放大发光
- **Material 材质响应**：光滑 3D 图标
- **Lighting 光学**：柔和顶光

## 提示词模板

```text
Grid wall of dozens of glossy rounded app icons with abstract generic symbols (no real brand logos), soft pastel colors, the central icon [HERO] enlarged and glowing, clean 3D render, top band empty for headline, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[HERO]` | 中心高亮图标，如 a sparkle star icon、a robot icon |

## 标题排版

- **中文区**：主标题 ≤ 14 字，必须含数字或结果；副标题写人群或场景；视觉元素只做辅助证据。
- **海外区**：海外区不推荐此家族，如必须使用，把字量压到一半。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 扁平图标化 | `flat iconographic character design, geometric simplification, two-color limited palette, app-icon feel, Material Design motion guidelines` |
| 平面设计 · 模块化网格 Modular Grid | `Layout on a strict modular grid, equal square modules, content blocks snapping to grid, clean systematic arrangement, swiss design influence, plenty of white space` |
| 三维渲染 · 影视级写实 | `cinematic, photorealistic, Arri Alexa, film grain, shallow depth of field, color graded, film look` |
| 动画 · 游戏技能图标循环 | `game skill icon loop, skill buff icon micro-loop, 1-3 seconds, 64x64 to 128x128 px, CD mask overlay, cooldown number` |
| 平面设计 · 栏式网格 Column Grid | `Editorial magazine page, six-column grid, body text flowing in columns, wide gutters, pull quotes spanning two columns, clean serif typography, structured` |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |

## 避坑

- AI 生成的中文字不可直接用：先出无字底图（标注留白区），再用 Figma/稿定/Canva 排字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
