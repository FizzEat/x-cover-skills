---
name: x-cover-cozy-anime-room
description: X 长文封面图：日系治愈书房（动漫与东方美学）。阳光书房里的猫咪和电脑，治愈、亲和。 适用 职场成长、AI 创作、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“日系治愈书房”风格时使用。
---

# 日系治愈书房

> 阳光书房里的猫咪和电脑，治愈、亲和。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | J · 动漫与东方美学 |
| 适用分类 | 职场成长、AI 创作、综合 |
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

- **Identity 身份**：日系治愈室内插画
- **Spatial 空间**：室内中景，窗外天空
- **Visual State 终端视觉状态**：阳光洒进书房，[CHARACTER] 在电脑前，旁边一只猫
- **Material 材质响应**：柔和水彩感上色
- **Lighting 光学**：午后暖光，光斑

## 提示词模板

```text
Cozy anime illustration, sunlit study room with bookshelves and plants, [CHARACTER] working at a computer, a cat napping on the desk, warm afternoon light and dappled shadows, soft watercolor-like coloring, peaceful slice-of-life, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[CHARACTER]` | 角色，如 a girl with headphones、a sleepy programmer |

## 标题排版

- **中文区**：标题用书法体或圆体，放在天空或纸面留白处，可加印章元素。
- **海外区**：小字，或直接用画面做钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 日系大眼 | `Japanese large anime eyes, multi-layer iris gradient highlights, clustered eyelashes, enlarged eye sockets, emotion amplifier, moe aesthetic, Kyoto Animation` |
| 三维渲染 · 极简/几何抽象 + 等距正交 + 高调纯色；循环无缝动画 | `motion graphics, looping animation, geometric shapes, mg, broadcast` |
| 电影画面 · 富士胶片暖调青阴影（Eterna感） | `Fujifilm Eterna look, cool cyan shadows, soft low contrast, muted greens, natural skin` |
| 动画 · 剪纸动画 | `paper cut-out stop-motion, articulated paper puppets, visible rivet joints, hard edges, paper fiber texture, folk art style` |
| 电影画面 · 婚礼宴会暖调热闹 | `wedding reception warm, string lights chandelier, laughing crowd, romantic celebration` |
| 动画 · 沙画动画 | `sand animation on backlit glass table, finger-smudged morphing, granular texture, earth tones, flowing metamorphosis, top-down view` |

## 避坑

- 不要写具体在世画师或动画公司名字，用风格描述（luminous anime sky, cel shading）替代。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
