---
name: x-cover-vaporwave-dream
description: X 长文封面图：蒸汽波梦境（宇宙科幻与未来视觉）。粉紫渐变、希腊石膏像、网格地平线，互联网怀旧梗图感。 适用 AI 创作、综合、做号变现 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“蒸汽波梦境”风格时使用。
---

# 蒸汽波梦境

> 粉紫渐变、希腊石膏像、网格地平线，互联网怀旧梗图感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | D · 宇宙科幻与未来视觉 |
| 适用分类 | AI 创作、综合、做号变现 |
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

- **Identity 身份**：蒸汽波互联网怀旧
- **Spatial 空间**：网格地平线 + 中央雕像
- **Visual State 终端视觉状态**：粉紫夕阳下的石膏像戴着 [PROP]，旁边漂浮 Windows 95 窗口
- **Material 材质响应**：石膏、塑料、CRT 扫描线
- **Lighting 光学**：粉紫渐变落日

## 提示词模板

```text
Vaporwave aesthetic, pink and purple sunset gradient, neon grid floor stretching to the horizon, a classical greek marble bust wearing [PROP], floating retro computer windows, palm trees, CRT scanlines, nostalgic internet dreamscape, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[PROP]` | 雕像道具，如 VR goggles、pixel sunglasses |

## 标题排版

- **中文区**：标题放在暗部天空区域，白色粗黑体，一句判断句。
- **海外区**：少字，大写无衬线短语（如 THE ENDGAME）。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 合成器浪潮/蒸汽波 | `synthwave, retrowave, magenta cyan gradient sky, grid horizon, sunset, palm trees, 80s` |
| 平面设计 · 蒸汽波 Vaporwave | `Vaporwave aesthetic artwork, pastel pink cyan purple sunset gradient, classical marble greek statue head, palm tree silhouette, japanese katakana text floating, retro computer window, VHS glitch, dreamy` |
| 平面设计 · Y2K 拟态 Y2K Aesthetics | `Y2K aesthetic poster, liquid chrome metallic blobs, holographic gradient background, translucent frosted plastic panels, windows 95 interface elements, futuristic optimistic, airbrushed, silver pink blue` |
| 三维渲染 · 渐变背景灯 | `gradient background, colored backdrop, studio gradient, color wash` |
| 三维渲染 · 程序化抽象 + 实验镜头 + 霓虹/渐变背景；高饱和强节奏 | `abstract 3D art, procedural forms, colorful, generative, modern art` |
| 三维渲染 · 产品级棚拍 + 无畸变正视 + 高调纯白/渐变背景；无干扰物 | `e-commerce hero image, amazon main image, white background product` |

## 避坑

- 避免廉价的蓝紫光污染和满屏粒子，保留大面积暗部给标题。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
