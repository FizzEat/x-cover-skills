---
name: x-cover-cheatsheet-table
description: X 长文封面图：速查表（中文区强文字转化）。一张整齐的速查表/参数表，“收藏起来慢慢看”。 适用 AI 编程、AI 创作、账号支付 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“速查表”风格时使用。
---

# 速查表

> 一张整齐的速查表/参数表，“收藏起来慢慢看”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | I · 中文区强文字转化 |
| 适用分类 | AI 编程、AI 创作、账号支付 |
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

- **Identity 身份**：速查表底图
- **Spatial 空间**：满版表格，表头高亮
- **Visual State 终端视觉状态**：[ROWS] 行表格，表头 [COLOR]，部分格子有勾和图标
- **Material 材质响应**：白卡片表格，细分割线
- **Lighting 光学**：平面

## 提示词模板

```text
Clean cheatsheet table infographic, [ROWS] rows with a [COLOR] header row, alternating light row shading, small icons and checkmarks in some cells, text placeholder bars, rounded card container, crisp vector, bookmark-worthy reference design, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ROWS]` | 行数 |
| `[COLOR]` | 表头颜色 |

## 标题排版

- **中文区**：主标题 ≤ 14 字，必须含数字或结果；副标题写人群或场景；视觉元素只做辅助证据。
- **海外区**：海外区不推荐此家族，如必须使用，把字量压到一半。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 新闻信息图动画 | `news infographic animation, news data/process explainer, fast turnaround, 15-60 seconds, big key numbers, source footnote, vertical social-first` |
| 平面设计 · 卡片式 Card Layout | `Card-based dashboard UI, grid of uniform cards each containing icon title and stats, subtle drop shadows, rounded corners, light gray background, clean modern SaaS style` |
| 平面设计 · 信息图 Infographic | `vertical infographic about climate change facts, clear headline, icon-based statistics, timeline chart, sources at bottom, educational shareable` |

## 避坑

- AI 生成的中文字不可直接用：先出无字底图（标注留白区），再用 Figma/稿定/Canva 排字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
