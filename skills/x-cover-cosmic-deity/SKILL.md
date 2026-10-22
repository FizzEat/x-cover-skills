---
name: x-cover-cosmic-deity
description: X 长文封面图：赛博巨神点描（宇宙科幻与未来视觉）。海外 AI 观察第一：前景一人，两侧人海，远处巨型 AI 神祇。 适用 AI 观察、综合 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“赛博巨神点描”风格时使用。
---

# 赛博巨神点描

> 海外 AI 观察第一：前景一人，两侧人海，远处巨型 AI 神祇。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | D · 宇宙科幻与未来视觉 |
| 适用分类 | AI 观察、综合 |
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

- **Identity 身份**：赛博反乌托邦史诗插画
- **Spatial 空间**：一点透视对称全景
- **Visual State 终端视觉状态**：前景 [FIGURE] 背影，两侧梯田人海对着发光屏幕，地平线上巨型数字神祇
- **Material 材质响应**：极细点描，无数微光屏幕
- **Lighting 光学**：神祇与屏幕同时发光

## 提示词模板

```text
Epic monumental visionary pointillism artwork, monochrome ink engraving style, symmetrical one-point perspective: in the foreground [FIGURE] seen from behind, vast terraced hillsides on both sides filled with thousands of people working on glowing laptops, a colossal transcendent cybernetic deity on the horizon with piercing glowing eyes, halo of network nodes and microchips, ultra-dense stippling, no text, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[FIGURE]` | 前景人物，如 a lone figure in a hoodie |

## 标题排版

- **中文区**：标题放在暗部天空区域，白色粗黑体，一句判断句。
- **海外区**：少字，大写无衬线短语（如 THE ENDGAME）。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 中心对称构图（韦斯·安德森式） | `centered symmetrical composition, Wes Anderson style, mirror balance, dead center` |
| 电影画面 · IMAX · 深景深史诗构图 | `IMAX epic deep focus, crystal clear foreground background, grand landscape` |
| 三维渲染 · 黑白单色 | `black and white, monochrome, grayscale, noir, desaturate` |
| 电影画面 · 镜面反射对称构图 | `mirror reflection symmetry, dual image, psychological split` |
| 电影画面 · 黑白高反差（Noir High Contrast） | `black and white high contrast noir, crushed blacks, hard bright highlights, dramatic shadows, film grain` |
| 电影画面 · 韦斯·安德森对称粉彩 | `Wes Anderson symmetrical pastels, centered composition, pastel palette, storybook flat` |

## 避坑

- 避免廉价的蓝紫光污染和满屏粒子，保留大面积暗部给标题。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
