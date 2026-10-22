---
name: x-cover-triple-candlestick
description: X 长文封面图：三联屏 K 线暴涨暴跌（机构研报与数据可视化）。三块屏幕的 K 线同时剧烈波动，制造“行情来了”的紧迫感。 适用 财经币圈 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“三联屏 K 线暴涨暴跌”风格时使用。
---

# 三联屏 K 线暴涨暴跌

> 三块屏幕的 K 线同时剧烈波动，制造“行情来了”的紧迫感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | B · 机构研报与数据可视化 |
| 适用分类 | 财经币圈 |
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

- **Identity 身份**：市场行情剧烈波动封面
- **Spatial 空间**：三块并排显示器，中间一块最大
- **Visual State 终端视觉状态**：红绿 K 线剧烈 [DIRECTION]，屏幕光映在桌面
- **Material 材质响应**：金属显示器边框，玻璃屏幕反光
- **Lighting 光学**：暗室，屏幕红绿光为唯一光源

## 提示词模板

```text
Three side-by-side trading monitors in a dark trading room, candlestick charts showing a dramatic [DIRECTION], glowing red and green candles, reflections on a glossy desk, cinematic shallow depth of field, tense atmosphere, financial thriller mood, screen light as the only light source, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[DIRECTION]` | 行情方向，如 parabolic surge、violent crash、V-shaped reversal |

## 标题排版

- **中文区**：标题写结论而不是话题（“算力需求 5 年翻 30 倍”），核心数字单独放大。
- **海外区**：英文衬线大标题 + 一条橙色短破折号，模仿卖方研报扉页。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 低调情绪暗场 | `dark moody, low key lighting, high contrast, chiaroscuro, dramatic shadows, film noir` |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 三维渲染 · 低调暗场 | `low key, dark mood, chiaroscuro, dramatic shadows, film noir` |

## 避坑

- 图表数字由 AI 生成大概率错，柱子和曲线只要形状，数字标签后期手动排。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
