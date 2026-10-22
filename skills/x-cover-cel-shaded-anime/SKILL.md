---
name: x-cover-cel-shaded-anime
description: X 长文封面图：赛璐璐动画角色（动漫与东方美学）。赛璐璐上色角色立绘，二次元受众友好。 适用 AI 创作、做号变现 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“赛璐璐动画角色”风格时使用。
---

# 赛璐璐动画角色

> 赛璐璐上色角色立绘，二次元受众友好。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | J · 动漫与东方美学 |
| 适用分类 | AI 创作、做号变现 |
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

- **Identity 身份**：赛璐璐动画角色
- **Spatial 空间**：角色半身居中偏右
- **Visual State 终端视觉状态**：[CHARACTER] 动态姿势，背景简洁
- **Material 材质响应**：赛璐璐两阶阴影，清晰线条
- **Lighting 光学**：平涂光

## 提示词模板

```text
Anime key visual, cel shaded [CHARACTER] in a dynamic pose, clean line art, two-tone shading, vibrant colors, simple gradient background with speed lines, right-weighted composition leaving left space for title, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[CHARACTER]` | 角色，如 a cyber girl with a holographic tablet |

## 标题排版

- **中文区**：标题用书法体或圆体，放在天空或纸面留白处，可加印章元素。
- **海外区**：小字，或直接用画面做钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 手绘赛璐璐 | `hand-painted cel animation on transparent celluloid, flat color fills, crisp outlines, vintage 1930s-90s cartoon, multiplane camera` |
| 三维渲染 · 卡通渲染 | `cel shaded, toon shader, flat colors, bold outlines, stepped shadows, cartoon` |
| 三维渲染 · 极简/几何抽象 + 等距正交 + 高调纯色；循环无缝动画 | `motion graphics, looping animation, geometric shapes, mg, broadcast` |
| 动画 · Pixar 角色表演体系 | `Pixar character performance system, believable physics simulation, subtle facial rigging brow-lip link, character-as-star storytelling, color script, CG animation` |
| 动画 · 赛璐璐两段影 | `cel two-tone shading, base color plus single shadow layer, hard-edged shadow boundary, standard anime coloring, two-step value` |
| 动画 · 剪纸动画 | `paper cut-out stop-motion, articulated paper puppets, visible rivet joints, hard edges, paper fiber texture, folk art style` |

## 避坑

- 不要写具体在世画师或动画公司名字，用风格描述（luminous anime sky, cel shading）替代。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
