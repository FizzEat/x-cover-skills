---
name: x-cover-chess-strategy
description: X 长文封面图：棋局博弈（超现实概念隐喻）。棋盘与棋子，讲战略、博弈、大厂竞争。 适用 财经币圈、AI 观察、职场成长 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“棋局博弈”风格时使用。
---

# 棋局博弈

> 棋盘与棋子，讲战略、博弈、大厂竞争。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | K · 超现实概念隐喻 |
| 适用分类 | 财经币圈、AI 观察、职场成长 |
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

- **Identity 身份**：棋局战略隐喻
- **Spatial 空间**：低角度贴近棋盘
- **Visual State 终端视觉状态**：[PIECES] 对峙，一枚棋子倒下
- **Material 材质响应**：大理石与金属棋子
- **Lighting 光学**：戏剧化顶光，暗背景

## 提示词模板

```text
Dramatic chess scene, low angle close to the board, [PIECES] facing off, one piece toppled, marble and metal textures, single dramatic top light, dark background, shallow depth of field, strategic tension, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[PIECES]` | 棋子设定，如 a robot king versus a human king |

## 标题排版

- **中文区**：标题用一句反问或判断，压在画面最安静的区域。
- **海外区**：无字或极小标题，隐喻本身就是标题。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 低调情绪暗场 | `dark moody, low key lighting, high contrast, chiaroscuro, dramatic shadows, film noir` |
| 三维渲染 · 顶光（上帝光） | `overhead light, top down lighting, god light, harsh overhead` |
| 三维渲染 · 浅景深微距 | `macro 100mm f/2.8, extreme close-up, shallow depth of field, focus plane` |
| 三维渲染 · 低调暗场 | `low key, dark mood, chiaroscuro, dramatic shadows, film noir` |
| 三维渲染 · 高调纯净 + 无畸变正视 + 均匀顶光；洁净塑料金属、无影 | `medical device render, clinical, clean, hospital equipment, sterile` |
| 三维渲染 · 景深合成 | `focus stack, all-in-focus macro, composite sharpness, depth blend` |

## 避坑

- 一个画面只放一个反常识，叠加两个以上隐喻会让读者看不懂。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
