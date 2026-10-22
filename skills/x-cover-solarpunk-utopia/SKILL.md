---
name: x-cover-solarpunk-utopia
description: X 长文封面图：太阳朋克乌托邦（宇宙科幻与未来视觉）。绿色未来城市，讲 AI 带来的乐观终局。 适用 AI 观察、职场成长 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“太阳朋克乌托邦”风格时使用。
---

# 太阳朋克乌托邦

> 绿色未来城市，讲 AI 带来的乐观终局。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | D · 宇宙科幻与未来视觉 |
| 适用分类 | AI 观察、职场成长 |
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

- **Identity 身份**：太阳朋克乌托邦城市
- **Spatial 空间**：俯瞰广角城市全景
- **Visual State 终端视觉状态**：绿植覆盖的白色建筑、太阳能帆、[DETAIL]
- **Material 材质响应**：白色曲面建筑，玻璃与植物
- **Lighting 光学**：明亮暖阳，通透空气

## 提示词模板

```text
Solarpunk utopian city panorama, white organic curved architecture covered in lush greenery, solar sails and wind turbines, [DETAIL], people walking in sunlit gardens, bright warm daylight, optimistic hopeful future, highly detailed concept art, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[DETAIL]` | 未来细节，如 friendly robots tending rooftop gardens |

## 标题排版

- **中文区**：标题放在暗部天空区域，白色粗黑体，一句判断句。
- **海外区**：少字，大写无衬线短语（如 THE ENDGAME）。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 高宽容度HDR自然主义 | `HDR naturalistic, neutral highlights, gentle roll-off, full shadow detail, true-to-life` |
| 三维渲染 · 高调纯净 | `high key, bright and airy, clean, minimal shadows, medical tech, sterile` |
| 三维渲染 · 概念艺术手绘风 | `concept art style, painterly brushstrokes, digital painting, artstation, loose edges, matte painting` |
| 电影画面 · ARRI Alexa · 自然肤色科学 | `shot on ARRI Alexa, natural skin tones, creamy highlights, cinematic digital` |
| 三维渲染 · 高调纯白 | `high key, pure white cyclorama, clean studio, bright` |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |

## 避坑

- 避免廉价的蓝紫光污染和满屏粒子，保留大面积暗部给标题。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
