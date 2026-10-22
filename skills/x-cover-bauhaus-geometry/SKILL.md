---
name: x-cover-bauhaus-geometry
description: X 长文封面图：包豪斯几何（极简编辑与书封海报）。红黄蓝三原色 + 圆方三角，构成感极强。 适用 AI 观察、AI 编程、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“包豪斯几何”风格时使用。
---

# 包豪斯几何

> 红黄蓝三原色 + 圆方三角，构成感极强。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | G · 极简编辑与书封海报 |
| 适用分类 | AI 观察、AI 编程、综合 |
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

- **Identity 身份**：包豪斯几何海报
- **Spatial 空间**：几何形组合构成
- **Visual State 终端视觉状态**：圆、方、三角构成 [FIGURE]
- **Material 材质响应**：平面纸张印刷
- **Lighting 光学**：无光影

## 提示词模板

```text
Bauhaus geometric poster, primary colors red yellow blue with black and cream, circles squares and triangles composing [FIGURE], bold modernist composition, flat print texture, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[FIGURE]` | 构成形象，如 an abstract robot face、a rising sun |

## 标题排版

- **中文区**：标题就是画面主角，使用宋体/思源宋体或粗黑体，字距收紧，严格对齐网格。
- **海外区**：大号衬线或 Grotesk 标题，配作者名和“Essay / Issue No.”等编辑元素。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 包豪斯 Bauhaus | `Bauhaus graphic design, geometric sans serif uppercase headline, asymmetric layout, red yellow blue accent blocks, photographic collage, white background, grid based composition` |
| 三维渲染 · 极简/几何抽象 + 等距正交 + 高调纯色；循环无缝动画 | `motion graphics, looping animation, geometric shapes, mg, broadcast` |
| 摄影 · 构成主义摄影 Constructivist photography | `constructivist photography 1920s Soviet, extreme high or low angle, diagonal composition, geometric abstraction, high contrast black and white, photomontage, wide angle perspective distortion, revolutionary propaganda` |
| 三维渲染 · 几何节点 | `geometry nodes, procedural modeling, instancing, modifier stack` |
| 平面设计 · 构成主义 Constructivism | `Russian Constructivism poster, dynamic diagonal layout, bold red black and white, photo montage, heavy sans-serif typography at angle, industrial smokestacks, revolutionary slogan` |
| 动画 · 美国 CalArts / Frederator 极简几何风 | `CalArts-influenced North American TV minimalism, rounded-rectangle body shapes, thick outline, minimal dot eyes slit mouth, flat bright colors, Adventure Time, Pendleton Ward` |

## 避坑

- 让 AI 只出版式底图和图形元素，标题文字一定后期排，AI 排字会破坏网格。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
