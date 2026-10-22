---
name: x-cover-checklist-card
description: X 长文封面图：Notion 清单打勾卡（工科蓝图与信息结构）。账号支付 TOP1 同款：暖白纸底 + 一张清单卡，每行一个图标一个对勾。 适用 账号支付、AI 编程、做号变现 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“Notion 清单打勾卡”风格时使用。
---

# Notion 清单打勾卡

> 账号支付 TOP1 同款：暖白纸底 + 一张清单卡，每行一个图标一个对勾。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | 账号支付、AI 编程、做号变现 |
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

- **Identity 身份**：知识博主清单交互卡封面
- **Spatial 空间**：左侧大字留白，右侧纵向高卡片
- **Visual State 终端视觉状态**：圆角卡片内 [N] 行清单，每行线条图标 + 文本占位 + 橙色对勾
- **Material 材质响应**：暖米白特种纸 #FAF7F2，12px 圆角，4% 灰度投影
- **Lighting 光学**：正面均匀无影柔光

## 提示词模板

```text
Minimalist editorial checklist banner, warm off-white cream paper texture background (#FAF7F2). Left side spacious empty area for bold title. Right side: a modern vertical rounded card with soft ambient shadow, inside [N] neat checklist rows, each with a minimalist monoline icon ([ICONS]), a short text placeholder bar and a warm terracotta orange checkmark. Notion-style aesthetic, Swiss editorial design, crisp vector clarity, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[N]` | 清单条数，建议 4~6 |
| `[ICONS]` | 每行图标，如 laptop, clock, SIM card, wifi, credit card |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 卡片式 Card Layout | `Card-based dashboard UI, grid of uniform cards each containing icon title and stats, subtle drop shadows, rounded corners, light gray background, clean modern SaaS style` |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 三维渲染 · 极简主义 | `minimalist, clean composition, negative space, monochrome palette, simple geometry` |
| 三维渲染 · 极简/几何抽象 + 等距正交 + 高调纯色；循环无缝动画 | `motion graphics, looping animation, geometric shapes, mg, broadcast` |
| 三维渲染 · 等距小场景/极简 + 正交相机 + 单柔光箱；圆润倒角柔和投影 | `3D icon, isometric icon, UI icon, app glyph, cute 3D` |
| 三维渲染 · 极简/粘土 + 正交正视 + 单侧柔光；识别度高、少细节 | `app icon, 3D glyph, cute 3D icon, simple, app store` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
