---
name: x-cover-storyboard-grid
description: X 长文封面图：分镜宫格（中文区强文字转化）。中文区 AI 创作第一同款：上半大片画面，下半 12 格分镜手稿。 适用 AI 创作 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“分镜宫格”风格时使用。
---

# 分镜宫格

> 中文区 AI 创作第一同款：上半大片画面，下半 12 格分镜手稿。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | I · 中文区强文字转化 |
| 适用分类 | AI 创作 |
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

- **Identity 身份**：电影大片 + 分镜表
- **Spatial 空间**：水平二分
- **Visual State 终端视觉状态**：上：[HERO_SCENE]；下：12 格铅笔分镜，带运镜箭头
- **Material 材质响应**：丝绸动态、木纹；分镜为纸面铅笔
- **Lighting 光学**：上部体积光，下部柔和纸面

## 提示词模板

```text
Split composition movie production banner. Top half: epic cinematic scene, [HERO_SCENE], dramatic volumetric god rays, rim light. Bottom half: a neat 12-frame director storyboard grid with black and white pencil sketch animatics, camera movement arrows, focal length notes, ultra detailed, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[HERO_SCENE]` | 上半主场景，如 a female wuxia warrior performing a flying kick inside an ancient wooden temple hall |

## 标题排版

- **中文区**：主标题 ≤ 14 字，必须含数字或结果；副标题写人群或场景；视觉元素只做辅助证据。
- **海外区**：海外区不推荐此家族，如必须使用，把字量压到一半。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 定焦标准视角（35/40/50mm） | `prime lens 50mm, natural perspective, human eye view, standard focal length` |
| 三维渲染 · 体积光与丁达尔 | `god rays, volumetric lighting, tyndall effect, light shafts, dust motes` |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 电影画面 · 超广角贴脸畸变 | `extreme wide-angle close-up, facial distortion, exaggerated nose, surreal intense` |
| 三维渲染 · 产品级写实 + 暗场点亮状态 + 自发光/体积光；IES 光域网 | `lighting fixture, lamp render, light on, IES profile, pendant` |
| 电影画面 · 长焦压缩窥视 | `telephoto compression, peeping perspective, shallow depth of field, distant observer` |

## 避坑

- AI 生成的中文字不可直接用：先出无字底图（标注留白区），再用 Figma/稿定/Canva 排字。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
