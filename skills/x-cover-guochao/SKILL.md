---
name: x-cover-guochao
description: X 长文封面图：国潮插画（动漫与东方美学）。传统纹样 + 高饱和撞色，国潮热度高。 适用 做号变现、AI 创作、综合 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“国潮插画”风格时使用。
---

# 国潮插画

> 传统纹样 + 高饱和撞色，国潮热度高。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | J · 动漫与东方美学 |
| 适用分类 | 做号变现、AI 创作、综合 |
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

- **Identity 身份**：国潮插画
- **Spatial 空间**：主体居中，祥云环绕
- **Visual State 终端视觉状态**：[SUBJECT] 搭配祥云、海浪纹、灯笼
- **Material 材质响应**：平涂与金色描边
- **Lighting 光学**：平面

## 提示词模板

```text
Chinese guochao trendy illustration, [SUBJECT] surrounded by auspicious clouds, wave patterns and lanterns, vibrant red, jade green and gold, flat colors with gold outlines, bold contemporary take on traditional motifs, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SUBJECT]` | 主体，如 a robot wearing a lion dance head |

## 标题排版

- **中文区**：标题用书法体或圆体，放在天空或纸面留白处，可加印章元素。
- **海外区**：小字，或直接用画面做钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 纹样与底纹 Patterns & Textures | `seamless geometric pattern texture, four-directional repeat, brand decorative motif, wrapping paper or fabric print application --tile` |

## 避坑

- 不要写具体在世画师或动画公司名字，用风格描述（luminous anime sky, cel shading）替代。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
