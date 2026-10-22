---
name: x-cover-chinese-poster-retro
description: X 长文封面图：老上海月份牌（动漫与东方美学）。民国月份牌广告画，复古商业感强。 适用 做号变现、财经币圈、综合 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“老上海月份牌”风格时使用。
---

# 老上海月份牌

> 民国月份牌广告画，复古商业感强。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | J · 动漫与东方美学 |
| 适用分类 | 做号变现、财经币圈、综合 |
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

- **Identity 身份**：老上海月份牌广告
- **Spatial 空间**：人物居中，四周装饰边框
- **Visual State 终端视觉状态**：[CHARACTER] 手持 [PRODUCT]，装饰花边
- **Material 材质响应**：擦笔水彩，柔和肤色
- **Lighting 光学**：柔光

## 提示词模板

```text
1930s Shanghai calendar poster advertisement, [CHARACTER] elegantly holding [PRODUCT], art deco ornamental border, soft airbrushed watercolor skin, pastel palette, vintage commercial art, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[CHARACTER]` | 人物，如 an elegant lady in qipao |
| `[PRODUCT]` | 手持物，如 a smartphone |

## 标题排版

- **中文区**：标题用书法体或圆体，放在天空或纸面留白处，可加印章元素。
- **海外区**：小字，或直接用画面做钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 九十年代早期 CG 复古 | `90s CGI, retro computer graphics, PS1 era, Gouraud shading, low res textures, VHS` |
| 平面设计 · 装饰艺术运动 Art Deco | `Art Deco poster 1920s, sunburst rays background, zigzag geometric border, gold foil accents, stylized fountain figure, elegant tall sans serif, luxurious, symmetrical` |
| 电影画面 · 复古褪色（Vintage Fade） | `vintage faded film, lifted blacks, milky highlights, aged color shift, film dust scratches` |
| 电影画面 · 复古镜头低反差眩光 | `vintage lens low contrast flare, hazy backlight, washed-out colors, retro` |
| 摄影 · Foma FOMAPAN RETROPAN 320 soft（黑白负片，ISO 320/26°，复古取向） | `Foma Retropan 320 soft ISO 320 black and white, retro look, soft contrast, rich midtones, fine grain, contact print aesthetic, vintage monochrome, D-76, still life architecture portrait, warm silver tone` |
| 动画 · 复古30年代弗拉珀风 | `1930s flapper era design, finger-wave curls, fringe dresses, slender limbs, rubber hose afterglow, jazz age art deco` |

## 避坑

- 不要写具体在世画师或动画公司名字，用风格描述（luminous anime sky, cel shading）替代。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
