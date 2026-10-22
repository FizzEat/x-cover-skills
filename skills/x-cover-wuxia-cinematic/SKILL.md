---
name: x-cover-wuxia-cinematic
description: X 长文封面图：武侠电影大片（动漫与东方美学）。古风武侠动作大片，AI 视频/影视创作长文高转化。 适用 AI 创作、综合 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“武侠电影大片”风格时使用。
---

# 武侠电影大片

> 古风武侠动作大片，AI 视频/影视创作长文高转化。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | J · 动漫与东方美学 |
| 适用分类 | AI 创作、综合 |
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

- **Identity 身份**：武侠电影动作场面
- **Spatial 空间**：中低机位仰拍
- **Visual State 终端视觉状态**：[ACTION]，衣袂与发丝飞扬
- **Material 材质响应**：丝绸动态褶皱，木质古建筑
- **Lighting 光学**：体积光，轮廓光

## 提示词模板

```text
Epic cinematic Chinese wuxia action scene, [ACTION], flowing silk robes and hair in motion, ancient wooden architecture, volumetric god rays, golden rim light, dust particles, low angle, Unreal Engine 5 render style, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ACTION]` | 动作场面，如 a swordswoman leaping across rooftops in the rain |

## 标题排版

- **中文区**：标题用书法体或圆体，放在天空或纸面留白处，可加印章元素。
- **海外区**：小字，或直接用画面做钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 三维渲染 · 体积光与丁达尔 | `god rays, volumetric lighting, tyndall effect, light shafts, dust motes` |
| 三维渲染 · 产品级写实 + 暗场点亮状态 + 自发光/体积光；IES 光域网 | `lighting fixture, lamp render, light on, IES profile, pendant` |
| 电影画面 · 雾气体积光（God Rays） | `fog volume light, god rays beams, atmospheric haze, cinematic shafts` |
| 电影画面 · 农场谷仓尘埃体积光 | `barn shafts of light through cracks, dust motes, warm rustic nostalgia` |
| 动画 · 体积光丁达尔 | `volumetric Tyndall light beams, visible light shafts, smoke dust haze medium, divine mysterious stage, god rays, crepuscular rays` |

## 避坑

- 不要写具体在世画师或动画公司名字，用风格描述（luminous anime sky, cel shading）替代。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
