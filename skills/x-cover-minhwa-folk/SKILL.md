---
name: x-cover-minhwa-folk
description: X 长文封面图：韩国民画（动漫与东方美学）。韩国民画的虎与喜鹊，色彩明快且有民俗趣味。 适用 AI 创作、综合 类长文，国内外通用。用户要做 X/推特长文封面、文章头图、公众号封面并想要“韩国民画”风格时使用。
---

# 韩国民画

> 韩国民画的虎与喜鹊，色彩明快且有民俗趣味。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | J · 动漫与东方美学 |
| 适用分类 | AI 创作、综合 |
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

- **Identity 身份**：韩国民画
- **Spatial 空间**：平面化构图，主体与配角对望
- **Visual State 终端视觉状态**：[ANIMAL] 与喜鹊、松树，造型夸张可爱
- **Material 材质响应**：韩纸矿物色
- **Lighting 光学**：平面

## 提示词模板

```text
Korean minhwa folk painting, a humorous [ANIMAL] with a magpie in a pine tree, flat decorative composition, bright mineral colors on hanji paper, naive charming style, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ANIMAL]` | 动物，如 tiger、a robot tiger（反差） |

## 标题排版

- **中文区**：标题用书法体或圆体，放在天空或纸面留白处，可加印章元素。
- **海外区**：小字，或直接用画面做钩子。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 电影画面 · 韩国类型片 | `Korean genre film, polished production, teal orange thriller, meticulous lighting, intense close-ups` |
| 动画 · 韩国网漫改编动画工业 | `Korean webtoon adaptation anime, vertical scroll panel adaptation, Korean urban fashion design, strong black-white contrast, Solo Leveling style, webtoon` |

## 避坑

- 不要写具体在世画师或动画公司名字，用风格描述（luminous anime sky, cel shading）替代。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
