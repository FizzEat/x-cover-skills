---
name: x-cover-isometric-room
description: X 长文封面图：3D 等轴小房间（3D 微缩与商业产品质感）。一间被剖开的等轴小房间，展示“一个人的工作流/一人公司”。 适用 AI 编程、做号变现、职场成长 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“3D 等轴小房间”风格时使用。
---

# 3D 等轴小房间

> 一间被剖开的等轴小房间，展示“一个人的工作流/一人公司”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 编程、做号变现、职场成长 |
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

- **Identity 身份**：3D 等轴剖面房间
- **Spatial 空间**：等轴 45 度单间剖面
- **Visual State 终端视觉状态**：[ROOM] 里摆满设备，屏幕亮着，一个小角色在工作
- **Material 材质响应**：柔和塑料与木质 3D 材质
- **Lighting 光学**：暖色室内灯 + 窗外蓝调

## 提示词模板

```text
Cute isometric 3D room cutaway, [ROOM], multiple glowing monitors, plants, shelves, cables, a small character working at the desk, soft clay-like materials, warm interior lamps with blue hour window light, Blender render, pastel palette, solid background, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ROOM]` | 房间设定，如 a one-person AI company studio、a streamer bedroom |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 影视级写实 | `cinematic, photorealistic, Arri Alexa, film grain, shallow depth of field, color graded, film look` |
| 三维渲染 · 卡通渲染 | `cel shaded, toon shader, flat colors, bold outlines, stepped shadows, cartoon` |
| 三维渲染 · 室内表现 + 人视 35mm + 窗口柔光；木材/织物材质真实 | `furniture render, sofa, interior staging, natural window light` |
| 三维渲染 · 产品级棚拍写实 | `studio lighting, pure white background, product photography, sharp focus, clean reflections, commercial shoot` |
| 电影画面 · 室内夜戏台灯 | `indoor night scene table lamp, warm pool of light, surrounding darkness, intimate conversation` |
| 三维渲染 · 三渲二 | `anime style, cel animation, Studio Ghibli aesthetic, expressive line art, manga` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
