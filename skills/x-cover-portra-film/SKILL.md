---
name: x-cover-portra-film
description: X 长文封面图：Portra 胶片日常（摄影与电影剧照）。温暖胶片色调的日常瞬间，温柔有温度。 适用 职场成长、AI 创作、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“Portra 胶片日常”风格时使用。
---

# Portra 胶片日常

> 温暖胶片色调的日常瞬间，温柔有温度。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | H · 摄影与电影剧照 |
| 适用分类 | 职场成长、AI 创作、综合 |
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

- **Identity 身份**：胶片日常摄影
- **Spatial 空间**：自然随意构图
- **Visual State 终端视觉状态**：[SCENE] 的日常瞬间
- **Material 材质响应**：Portra 400 柔和肤色与颗粒
- **Lighting 光学**：午后自然光

## 提示词模板

```text
Kodak Portra 400 film photograph, warm natural skin tones, soft grain, [SCENE], candid everyday moment, golden afternoon light, nostalgic and gentle, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SCENE]` | 场景，如 a person reading on a sunlit balcony with a laptop |

## 标题排版

- **中文区**：选主体偏一侧的画面，在暗部或天空放白字，必要时加 20% 黑色渐变压暗。
- **海外区**：无字或电影海报式底部小字。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 胶片调色 LUT | `film LUT, Kodak 2383, Fuji Eterna, cine grade, movie look` |
| 电影画面 · 自然光写实 | `natural available light, realistic daylight, no visible film lighting` |
| 电影画面 · 富士胶片暖调青阴影（Eterna感） | `Fujifilm Eterna look, cool cyan shadows, soft low contrast, muted greens, natural skin` |
| 三维渲染 · 超现实/抽象 + 方形构图 + 特殊胶片 LUT；艺术感强 | `album cover, music artwork, surreal 3D, vinyl cover art` |
| 电影画面 · 达内兄弟手持自然光纪实 | `Dardenne brothers handheld natural light, following behind shoulder, social realism, working class` |
| 电影画面 · 婚礼宴会暖调热闹 | `wedding reception warm, string lights chandelier, laughing crowd, romantic celebration` |

## 避坑

- 避免网红滤镜和过度磨皮；人物不要直视镜头摆拍，抓拍感更像真实故事。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
