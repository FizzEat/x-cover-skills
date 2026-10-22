---
name: x-cover-comic-panels
description: X 长文封面图：美漫分格（手绘插画与漫画叙事）。四格美漫讲一个转折故事，最后一格是反转。 适用 AI 观察、综合、做号变现 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“美漫分格”风格时使用。
---

# 美漫分格

> 四格美漫讲一个转折故事，最后一格是反转。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | AI 观察、综合、做号变现 |
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

- **Identity 身份**：美式漫画分格叙事
- **Spatial 空间**：2x2 分格，最后一格放大
- **Visual State 终端视觉状态**：四格依次 [STORY]
- **Material 材质响应**：网点上色，粗墨线
- **Lighting 光学**：戏剧化漫画光

## 提示词模板

```text
American comic book page, 2x2 panel grid with the last panel enlarged, bold ink outlines, Ben-Day dot shading, vibrant primary colors, four beats: [STORY], dynamic angles, empty speech balloons, action lines, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[STORY]` | 四格剧情，如 hero struggles with spreadsheets / discovers AI / automates everything / ends up bored on a beach |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 少女漫画长线条 | `shojo manga flowing line style, long flowing multi-strand hair, slender limbs, ornate clustered eyelashes, fine hatching, CLAMP, Naoko Takeuchi` |
| 动画 · 漫画网点化造型 | `manga screentone-styled design, halftone dot fills, hatching shadows, speed line backgrounds, speech balloons, onomatopoeia` |
| 电影画面 · 高饱和 · 波普糖果色版 | `pop art candy colors, pastel pink mint yellow, hyper saturated, Wes Anderson playful` |
| 动画 · 网点半调 | `screentone halftone texture, printed halftone dots, manga print feel, rosette moire pattern, pop art` |
| 平面设计 · 高饱和波普 Pop Art Saturated | `pop art comic panel poster, bold primary red yellow blue flat colors, thick black outlines, Ben-Day dot shading, Roy Lichtenstein inspired` |
| 平面设计 · 半调网点 Halftone | `vintage concert poster with halftone dot portrait shading, CMYK rosette pattern magnified, retro gig flyer aesthetic` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
