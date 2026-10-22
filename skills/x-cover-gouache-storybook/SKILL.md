---
name: x-cover-gouache-storybook
description: X 长文封面图：水粉绘本（手绘插画与漫画叙事）。儿童绘本般的水粉笔触，温柔讲道理。 适用 职场成长、综合、AI 创作 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“水粉绘本”风格时使用。
---

# 水粉绘本

> 儿童绘本般的水粉笔触，温柔讲道理。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | 职场成长、综合、AI 创作 |
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

- **Identity 身份**：温暖水粉绘本插画
- **Spatial 空间**：主角在画面三分点
- **Visual State 终端视觉状态**：[CHARACTER] 在 [PLACE]，周围细节富有童趣
- **Material 材质响应**：不透明水粉，可见笔触，纸纹
- **Lighting 光学**：柔和午后暖光

## 提示词模板

```text
Gouache children's picture book illustration, visible opaque brush strokes, [CHARACTER] in [PLACE], whimsical details, warm afternoon light, muted harmonious palette, cozy and gentle storytelling, textured paper, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[CHARACTER]` | 角色，如 a small fox learning to code |
| `[PLACE]` | 地点，如 a treehouse library |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 儿童绘本翻页动画 | `children's picture book flipbook animation, digitized picture book, realistic page-turn or swipe, child voice narration, tap-triggered hotspots, parent-child co-reading` |
| 三维渲染 · 水彩插画风 | `watercolor illustration, paper texture, pigment bloom, wet-on-wet, soft edges, hand drawn` |
| 平面设计 · 有限色扁平插画调色盘 Limited Flat Palette | `flat illustration set with limited 5-color palette, isometric office scenes, clean vector, SaaS onboarding illustrations, consistent branding` |
| 平面设计 · 插画主导 Illustration-Led | `flat vector illustration website hero, diverse characters collaborating around giant laptop, bright brand colors, SaaS onboarding` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
