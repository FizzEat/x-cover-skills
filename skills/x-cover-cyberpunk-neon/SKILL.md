---
name: x-cover-cyberpunk-neon
description: X 长文封面图：赛博朋克霓虹街（宇宙科幻与未来视觉）。雨夜霓虹、全息广告，讲 AI 渗透日常与高科技低生活。 适用 AI 观察、AI 编程、财经币圈 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“赛博朋克霓虹街”风格时使用。
---

# 赛博朋克霓虹街

> 雨夜霓虹、全息广告，讲 AI 渗透日常与高科技低生活。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | D · 宇宙科幻与未来视觉 |
| 适用分类 | AI 观察、AI 编程、财经币圈 |
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

- **Identity 身份**：赛博朋克城市夜景
- **Spatial 空间**：低角度仰拍狭窄街道
- **Visual State 终端视觉状态**：雨夜街头，全息广告显示 [HOLOGRAM]，行人撑伞
- **Material 材质响应**：湿漉漉地面反射霓虹
- **Lighting 光学**：品红与青色霓虹，体积雾

## 提示词模板

```text
Cinematic cyberpunk street at night, rain-soaked pavement reflecting neon, towering buildings covered in holographic advertisements showing [HOLOGRAM], pedestrians with umbrellas, magenta and cyan neon, volumetric fog, low angle, anamorphic lens flare, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[HOLOGRAM]` | 全息广告内容，如 a giant AI assistant face、a crypto price ticker |

## 标题排版

- **中文区**：标题放在暗部天空区域，白色粗黑体，一句判断句。
- **海外区**：少字，大写无衬线短语（如 THE ENDGAME）。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 赛博朋克霓虹 | `cyberpunk, neon lights, wet streets, purple cyan orange, holographic, futuristic city` |
| 三维渲染 · 霓虹自发光 | `neon lights, glowing tubes, cyberpunk lighting, self-lit signage` |
| 电影画面 · 透过介质拍摄（雨窗/纱帘/蒸汽） | `shooting through rain-streaked window, sheer curtain diffusion, steam fog` |
| 三维渲染 · 电影感/概念艺术 + 广角冲击 + 青橙或胶片 LUT；标题留白 | `movie poster, key visual, cinematic poster, blockbuster, title space` |
| 三维渲染 · 赛博朋克/抽象 + 任意风格镜头 + 霓虹自发光明暗对比 | `NFT artwork, 3D collectible, crypto art, digital art, 1/1` |
| 三维渲染 · 程序化抽象 + 实验镜头 + 霓虹/渐变背景；高饱和强节奏 | `abstract 3D art, procedural forms, colorful, generative, modern art` |

## 避坑

- 避免廉价的蓝紫光污染和满屏粒子，保留大面积暗部给标题。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
