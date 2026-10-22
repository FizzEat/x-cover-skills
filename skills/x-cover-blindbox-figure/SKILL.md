---
name: x-cover-blindbox-figure
description: X 长文封面图：潮玩盲盒手办（3D 微缩与商业产品质感）。把作者或概念做成潮玩盲盒，配包装盒，小红书 X 双平台都吃香。 适用 AI 创作、做号变现、综合 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“潮玩盲盒手办”风格时使用。
---

# 潮玩盲盒手办

> 把作者或概念做成潮玩盲盒，配包装盒，小红书 X 双平台都吃香。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 创作、做号变现、综合 |
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

- **Identity 身份**：潮玩盲盒产品图
- **Spatial 空间**：手办居中，旁边包装盒
- **Visual State 终端视觉状态**：[CHARACTER] 潮玩手办站在展台上，身后是印着角色的盒子
- **Material 材质响应**：光滑 PVC 与哑光涂装
- **Lighting 光学**：棚拍柔光，轻微反射

## 提示词模板

```text
Collectible designer toy figure, chibi proportions, [CHARACTER] standing on a small display base next to its matching blind box packaging, glossy PVC and matte paint, pastel studio background, soft studio lighting, product photography, cute and premium, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[CHARACTER]` | 角色，如 a programmer with a hoodie and a tiny laptop |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 三维渲染 · 产品级棚拍写实 + 无畸变正视或 3/4 视角 + 三点布光/高调纯白；材质如实还原 | `product visualization, studio render, hero shot, e-commerce, packaging` |
| 三维渲染 · 卡通渲染 | `cel shaded, toon shader, flat colors, bold outlines, stepped shadows, cartoon` |
| 三维渲染 · 无畸变产品正视 | `product front view, zero distortion, telecentric look, orthogonal shot` |
| 三维渲染 · 产品级棚拍 + 无畸变正视 + 高调纯白/渐变背景；无干扰物 | `e-commerce hero image, amazon main image, white background product` |
| 三维渲染 · 产品级写实 + 45° 3/4 视角 + 柔光箱；可替换标签贴图 | `packaging mockup, box mockup, label design, product shot` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
