---
name: x-cover-terminal-dashboard
description: X 长文封面图：彭博终端多面板（机构研报与数据可视化）。琥珀色等宽字 + 密集面板，彭博终端的专业冷感。 适用 财经币圈、AI 观察 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“彭博终端多面板”风格时使用。
---

# 彭博终端多面板

> 琥珀色等宽字 + 密集面板，彭博终端的专业冷感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | B · 机构研报与数据可视化 |
| 适用分类 | 财经币圈、AI 观察 |
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

- **Identity 身份**：专业金融终端数据封面
- **Spatial 空间**：密排信息墙，多面板网格
- **Visual State 终端视觉状态**：多个面板显示折线、热力格、滚动行情条，中心一个面板高亮 [FOCUS]
- **Material 材质响应**：黑底琥珀色/橙色等宽像素字体
- **Lighting 光学**：屏幕自发光

## 提示词模板

```text
Retro professional financial terminal interface, dense information wall of black panels with amber and orange monospace text textures, line charts, heatmap grids, scrolling ticker tape, one central panel highlighted showing [FOCUS], CRT glow, data-dense institutional aesthetic, sharp and serious, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[FOCUS]` | 高亮面板内容，如 a rising GPU index chart、a yield curve |

## 标题排版

- **中文区**：标题写结论而不是话题（“算力需求 5 年翻 30 倍”），核心数字单独放大。
- **海外区**：英文衬线大标题 + 一条橙色短破折号，模仿卖方研报扉页。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 密排信息墙 Information Wall | `Dense information wall poster, wall of tightly set small type covering most of the page, minimal hierarchy, monospaced typography, encyclopedia aesthetic, overwhelming data texture` |
| 平面设计 · 早期数字点阵 Early Digital / Bitstream | `1980s early desktop publishing zine, dot matrix printer texture, pixelated bitmap fonts, laser print toner speckle, monochrome green or amber screen aesthetic, raw scan` |

## 避坑

- 图表数字由 AI 生成大概率错，柱子和曲线只要形状，数字标签后期手动排。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
