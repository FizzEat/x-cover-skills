---
name: x-cover-street-leica
description: X 长文封面图：徕卡街拍（摄影与电影剧照）。黑白街头抓拍，决定性瞬间，真实人生感。 适用 职场成长、综合、做号变现 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“徕卡街拍”风格时使用。
---

# 徕卡街拍

> 黑白街头抓拍，决定性瞬间，真实人生感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | H · 摄影与电影剧照 |
| 适用分类 | 职场成长、综合、做号变现 |
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

- **Identity 身份**：黑白街头纪实
- **Spatial 空间**：35mm 视角，几何构图
- **Visual State 终端视觉状态**：城市街头 [MOMENT]，光影切割
- **Material 材质响应**：高对比黑白胶片颗粒
- **Lighting 光学**：硬朗阳光与长影

## 提示词模板

```text
Black and white street photography, 35mm rangefinder look, decisive moment: [MOMENT], strong geometric shadows, high contrast Tri-X film grain, candid and authentic, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[MOMENT]` | 瞬间，如 a commuter staring at their phone under a huge billboard |

## 标题排版

- **中文区**：选主体偏一侧的画面，在暗部或天空放白字，必要时加 20% 黑色渐变压暗。
- **海外区**：无字或电影海报式底部小字。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 去饱和 · 冷灰新闻纪实版 | `docudrama cold gray, news footage aesthetic, desaturated greens, slightly harsh contrast` |
| 三维渲染 · 黑白单色 | `black and white, monochrome, grayscale, noir, desaturate` |
| 三维渲染 · 胶片调色 LUT | `film LUT, Kodak 2383, Fuji Eterna, cine grade, movie look` |
| 电影画面 · 达内兄弟手持自然光纪实 | `Dardenne brothers handheld natural light, following behind shoulder, social realism, working class` |
| 电影画面 · 黑白高反差（Noir High Contrast） | `black and white high contrast noir, crushed blacks, hard bright highlights, dramatic shadows, film grain` |
| 三维渲染 · 超现实/抽象 + 方形构图 + 特殊胶片 LUT；艺术感强 | `album cover, music artwork, surreal 3D, vinyl cover art` |

## 避坑

- 避免网红滤镜和过度磨皮；人物不要直视镜头摆拍，抓拍感更像真实故事。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
