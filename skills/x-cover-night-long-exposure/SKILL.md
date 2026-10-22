---
name: x-cover-night-long-exposure
description: X 长文封面图：夜城长曝光（摄影与电影剧照）。城市光轨与高楼，讲速度、规模和城市里的奋斗。 适用 AI 观察、财经币圈、职场成长 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“夜城长曝光”风格时使用。
---

# 夜城长曝光

> 城市光轨与高楼，讲速度、规模和城市里的奋斗。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | H · 摄影与电影剧照 |
| 适用分类 | AI 观察、财经币圈、职场成长 |
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

- **Identity 身份**：城市夜景长曝光
- **Spatial 空间**：高处俯拍街道或天际线
- **Visual State 终端视觉状态**：车流光轨穿过 [CITY]，高楼灯光
- **Material 材质响应**：光轨拖影，湿润路面
- **Lighting 光学**：蓝调时刻 + 人造光

## 提示词模板

```text
Long exposure night cityscape of [CITY] from a high vantage point, streaming light trails of traffic, glowing skyscrapers, blue hour sky, wet reflective streets, sense of speed and scale, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[CITY]` | 城市，如 Shanghai Lujiazui、Shenzhen、Tokyo |

## 标题排版

- **中文区**：选主体偏一侧的画面，在暗部或天空放白字，必要时加 20% 黑色渐变压暗。
- **海外区**：无字或电影海报式底部小字。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 蓝调时刻（Blue Hour） | `blue hour twilight, deep blue sky, city lights on, warm windows contrast` |
| 三维渲染 · 影视写实 + 长焦压缩/低角度 + 日落逆光或城市 HDRI；车漆清漆层、镀铬 | `car render, automotive, vehicle design, sunset rim light, supercar` |
| 电影画面 · 35mm · 500T夜景推冲粗颗粒 | `pushed 500T night, heavy film grain, gritty shadows, nocturnal` |
| 摄影 · 蓝调时刻 Blue Hour | `cityscape at dusk, blue hour, cool blue sky, streetlights on, soft even light, neon signs, long exposure, light trails, teal and orange, medium format, Fujifilm Provia 100F, twilight mood, urban night` |
| 电影画面 · 天台城市天际线夜景 | `rooftop skyline night, city bokeh background, wind, freedom or loneliness, urban vastness` |

## 避坑

- 避免网红滤镜和过度磨皮；人物不要直视镜头摆拍，抓拍感更像真实故事。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
