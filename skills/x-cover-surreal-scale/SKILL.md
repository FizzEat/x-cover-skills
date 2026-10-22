---
name: x-cover-surreal-scale
description: X 长文封面图：巨物错位（超现实概念隐喻）。日常物件放大成建筑尺度，人变得极小。 适用 AI 观察、综合、职场成长 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“巨物错位”风格时使用。
---

# 巨物错位

> 日常物件放大成建筑尺度，人变得极小。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | K · 超现实概念隐喻 |
| 适用分类 | AI 观察、综合、职场成长 |
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

- **Identity 身份**：超现实尺度错位
- **Spatial 空间**：低视角，巨物占画面主体
- **Visual State 终端视觉状态**：巨大的 [OBJECT] 矗立在 [PLACE]，小人仰望
- **Material 材质响应**：物件真实材质
- **Lighting 光学**：自然光，长影

## 提示词模板

```text
Surreal scale illustration, a gigantic [OBJECT] towering over [PLACE], tiny people looking up at it, realistic materials, long shadows, dreamlike yet photoreal, conceptual art, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[OBJECT]` | 巨物，如 smartphone、coffee cup、cursor arrow |
| `[PLACE]` | 场景，如 a city square |

## 标题排版

- **中文区**：标题用一句反问或判断，压在画面最安静的区域。
- **海外区**：无字或极小标题，隐喻本身就是标题。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 超现实梦幻 | `surreal, dreamlike, floating objects, impossible scale, soft focus, ethereal, fantasy` |
| 三维渲染 · 概念艺术手绘风 | `concept art style, painterly brushstrokes, digital painting, artstation, loose edges, matte painting` |
| 三维渲染 · 超现实/抽象 + 方形构图 + 特殊胶片 LUT；艺术感强 | `album cover, music artwork, surreal 3D, vinyl cover art` |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 摄影 · 超现实主义摄影 Surrealist photography | `surrealist photography 1920s, rayograph photogram, solarization, Man Ray, high contrast negative effect, dreamlike double exposure, disembodied objects, avant-garde Paris, experimental darkroom` |

## 避坑

- 一个画面只放一个反常识，叠加两个以上隐喻会让读者看不懂。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
