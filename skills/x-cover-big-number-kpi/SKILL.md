---
name: x-cover-big-number-kpi
description: X 长文封面图：巨型数字 KPI（机构研报与数据可视化）。整张图只有一个巨大的数字，其余全部服务于它。 适用 做号变现、财经币圈、职场成长 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“巨型数字 KPI”风格时使用。
---

# 巨型数字 KPI

> 整张图只有一个巨大的数字，其余全部服务于它。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | B · 机构研报与数据可视化 |
| 适用分类 | 做号变现、财经币圈、职场成长 |
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

- **Identity 身份**：单一核心数字冲击封面
- **Spatial 空间**：数字占画面 60%，居中或偏左
- **Visual State 终端视觉状态**：巨型 3D 数字 [NUMBER]，旁边一条上升曲线与小注释位
- **Material 材质响应**：铬金属或玻璃材质数字，暗底
- **Lighting 光学**：顶光 + 边缘轮廓光

## 提示词模板

```text
Giant bold 3D number '[NUMBER]' dominating the frame, made of [MATERIAL], a thin glowing upward line chart sweeping behind it, small annotation placeholder lines, dark minimal background, dramatic top light and rim light, high-end financial results announcement aesthetic, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[NUMBER]` | 核心数字，如 10x、$1M、30 天（建议用阿拉伯数字，后期替换更稳） |
| `[MATERIAL]` | 数字材质，如 polished chrome、frosted glass、gold |

## 标题排版

- **中文区**：标题写结论而不是话题（“算力需求 5 年翻 30 倍”），核心数字单独放大。
- **海外区**：英文衬线大标题 + 一条橙色短破折号，模仿卖方研报扉页。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 三维渲染 · 镜面抛光金属（铬/银） | `mirror chrome, polished silver, flawless reflections, high reflectivity` |
| 三维渲染 · 影视写实 + 长焦压缩/低角度 + 日落逆光或城市 HDRI；车漆清漆层、镀铬 | `car render, automotive, vehicle design, sunset rim light, supercar` |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 三维渲染 · 极简/金属质感 + 特写 + 边缘光/霓虹；品牌标准色 | `logo reveal, brand identity, metallic logo, typography 3D` |
| 三维渲染 · 产品级写实 + 微距 + 多柔光箱/AOI 摄影棚；金属高抛、宝石焦散 | `jewelry render, watch macro, diamond caustics, gold polished, luxury` |
| 三维渲染 · 高调纯净 + 无畸变正视 + 均匀顶光；洁净塑料金属、无影 | `medical device render, clinical, clean, hospital equipment, sterile` |

## 避坑

- 图表数字由 AI 生成大概率错，柱子和曲线只要形状，数字标签后期手动排。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
