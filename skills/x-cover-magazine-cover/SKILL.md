---
name: x-cover-magazine-cover
description: X 长文封面图：时代周刊式杂志封面（极简编辑与书封海报）。红框杂志封面 + 一个人物/物体，“年度人物”感。 适用 AI 观察、职场成长、财经币圈 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“时代周刊式杂志封面”风格时使用。
---

# 时代周刊式杂志封面

> 红框杂志封面 + 一个人物/物体，“年度人物”感。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | G · 极简编辑与书封海报 |
| 适用分类 | AI 观察、职场成长、财经币圈 |
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

- **Identity 身份**：新闻周刊封面
- **Spatial 空间**：红色粗边框，主体居中
- **Visual State 终端视觉状态**：[SUBJECT] 正面肖像式构图，严肃
- **Material 材质响应**：铜版纸光泽
- **Lighting 光学**：棚拍伦勃朗光

## 提示词模板

```text
News magazine cover design, thick red border frame, [SUBJECT] centered in a dramatic portrait composition, serious tone, studio Rembrandt lighting, glossy paper, empty masthead area at top and cover lines placeholder, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[SUBJECT]` | 主体，如 a humanoid robot in a suit、a glowing AI chip |

## 标题排版

- **中文区**：标题就是画面主角，使用宋体/思源宋体或粗黑体，字距收紧，严格对齐网格。
- **海外区**：大号衬线或 Grotesk 标题，配作者名和“Essay / Issue No.”等编辑元素。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 杂志跨页 Magazine Spread | `Luxury magazine double page spread, full-bleed hero image spanning both pages across gutter, kicker text top left, large serif headline, elegant fashion editorial look` |
| 三维渲染 · 伦勃朗光 | `rembrandt lighting, triangle light, dramatic portrait, painterly light` |
| 平面设计 · Didot / HTF Didot（时尚杂志现代体） | `Didot perfume advertisement, French modern serif headline, minimalist glass bottle, marble background, high fashion editorial` |
| 三维渲染 · 影视写实或三渲二 + 85mm 人像 + 三点布光/伦勃朗；皮肤 SSS、毛发 groom | `character render, portrait, realistic human, stylized character, hero` |
| 平面设计 · 杂志 Magazine Editorial | `luxury fashion magazine spread, full-bleed image across gutter, large serif headline, layered captions, editorial typography` |
| 电影画面 · 伦勃朗三点布光 | `Rembrandt three-point lighting, triangle cheek light, classic portrait` |

## 避坑

- 让 AI 只出版式底图和图形元素，标题文字一定后期排，AI 排字会破坏网格。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
