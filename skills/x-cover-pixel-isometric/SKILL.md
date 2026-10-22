---
name: x-cover-pixel-isometric
description: X 长文封面图：等轴像素小世界（手绘插画与漫画叙事）。像素风小办公室/小城市，游戏感带来亲和力。 适用 AI 编程、做号变现、AI 创作 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“等轴像素小世界”风格时使用。
---

# 等轴像素小世界

> 像素风小办公室/小城市，游戏感带来亲和力。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | E · 手绘插画与漫画叙事 |
| 适用分类 | AI 编程、做号变现、AI 创作 |
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

- **Identity 身份**：等轴像素艺术场景
- **Spatial 空间**：等轴 45 度小岛或房间
- **Visual State 终端视觉状态**：像素小人在 [SCENE] 里各司其职
- **Material 材质响应**：像素颗粒，有限色板
- **Lighting 光学**：像素化柔光与小灯

## 提示词模板

```text
Isometric pixel art diorama, cozy [SCENE], tiny pixel characters busy working, small glowing monitors, plants and cables, limited warm palette, crisp pixel edges, retro game aesthetic, floating island on a solid background, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SCENE]` | 场景，如 AI startup office、creator studio、server room |

## 标题排版

- **中文区**：手写感标题 + 马克笔下划线，步骤编号用圆圈数字。
- **海外区**：New Yorker 式小标或直接无字，让漫画的冲突场景成为钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 像素化三维 | `pixelated 3D, voxel surface, 8-bit colors, retro game assets, Minecraft style` |
| 平面设计 · 早期数字点阵 Early Digital / Bitstream | `1980s early desktop publishing zine, dot matrix printer texture, pixelated bitmap fonts, laser print toner speckle, monochrome green or amber screen aesthetic, raw scan` |
| 三维渲染 · 实时游戏引擎风格 | `Unreal Engine 5 render, real-time, Lumen, Nanite, game asset showcase, screen space` |
| 动画 · 像素动画 | `pixel art animation, low-res pixel grid, limited color palette, dithering transitions, retro game sprite, 16-bit SNES GBA style` |
| 三维渲染 · 影视写实/写实游戏风 + 广角 + 日光+体积雾；大气透视层次 | `environment design, landscape, epic scenery, atmospheric fog, vista` |
| 动画 · 游戏像素精灵序列 | `game pixel sprite sheet sequence, character action sprites, fixed canvas 32x32, frame texture atlas, pivot aligned at feet, attack hit directions` |

## 避坑

- 手绘图标不要超过 6 个，否则信息噪音压过标题；AI 写的手写字基本不可读，后期补字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
