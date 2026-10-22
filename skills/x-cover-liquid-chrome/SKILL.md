---
name: x-cover-liquid-chrome
description: X 长文封面图：液态铬金属（3D 微缩与商业产品质感）。流动的液态金属雕塑，未来感品牌视觉。 适用 AI 创作、AI 观察 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“液态铬金属”风格时使用。
---

# 液态铬金属

> 流动的液态金属雕塑，未来感品牌视觉。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 创作、AI 观察 |
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

- **Identity 身份**：液态铬抽象雕塑
- **Spatial 空间**：主体居中，流体环绕
- **Visual State 终端视觉状态**：液态铬塑形为 [SHAPE]，表面映出环境
- **Material 材质响应**：镜面铬，彩虹反射
- **Lighting 光学**：HDRI 环境光，锐利高光

## 提示词模板

```text
Liquid chrome abstract sculpture flowing into the shape of [SHAPE], mirror-like reflective surface with iridescent highlights, smooth fluid dynamics, dark gradient background, HDRI studio reflections, Y2K futuristic brand visual, 3D render, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SHAPE]` | 塑形，如 a human head、an infinity loop |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 镜面抛光金属（铬/银） | `mirror chrome, polished silver, flawless reflections, high reflectivity` |
| 三维渲染 · 极简/金属质感 + 特写 + 边缘光/霓虹；品牌标准色 | `logo reveal, brand identity, metallic logo, typography 3D` |
| 平面设计 · Y2K 拟态 Y2K Aesthetics | `Y2K aesthetic poster, liquid chrome metallic blobs, holographic gradient background, translucent frosted plastic panels, windows 95 interface elements, futuristic optimistic, airbrushed, silver pink blue` |
| 三维渲染 · 影视级写实 | `cinematic, photorealistic, Arri Alexa, film grain, shallow depth of field, color graded, film look` |
| 三维渲染 · 影视写实 + 长焦压缩/低角度 + 日落逆光或城市 HDRI；车漆清漆层、镀铬 | `car render, automotive, vehicle design, sunset rim light, supercar` |
| 三维渲染 · 产品级写实 + 微距 + 多柔光箱/AOI 摄影棚；金属高抛、宝石焦散 | `jewelry render, watch macro, diamond caustics, gold polished, luxury` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
