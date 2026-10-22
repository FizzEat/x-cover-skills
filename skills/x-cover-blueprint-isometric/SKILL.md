---
name: x-cover-blueprint-isometric
description: X 长文封面图：白底蓝图等轴测三段流（工科蓝图与信息结构）。中文区 AI 编程第一名同款：左字右图，三张等轴测卡片讲清“输入→编排→产出”。 适用 AI 编程、做号变现、AI 创作 类长文，中文区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“白底蓝图等轴测三段流”风格时使用。
---

# 白底蓝图等轴测三段流

> 中文区 AI 编程第一名同款：左字右图，三张等轴测卡片讲清“输入→编排→产出”。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | A · 工科蓝图与信息结构 |
| 适用分类 | AI 编程、做号变现、AI 创作 |
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

- **Identity 身份**：极简科技生产力指南封面，工科蓝图感
- **Spatial 空间**：左 40% 留白排字，右 60% 三段等轴测流程，30 度轴测角
- **Visual State 终端视觉状态**：三张浮空线框卡片由细蓝箭头串联：[STEP_1]→[STEP_2]→[STEP_3]
- **Material 材质响应**：纯白哑光底，钴蓝细线，半透明磨砂玻璃卡片
- **Lighting 光学**：均匀环境柔光，卡片下方极浅弥散阴影

## 提示词模板

```text
Clean minimalist tech blueprint banner, pure crisp white background. Left side reserved empty for bold typography. Right side: a sequence of three isometric technical UI diagrams connected by thin cobalt blue directional arrows: [STEP_1], [STEP_2], [STEP_3]. Thin vector wireframes, translucent frosted glass plates, cobalt blue (#2563EB) and slate gray accent lines, subtle soft contact shadows, ultra-clean enterprise productivity aesthetic, ruler tick marks along the edges, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[STEP_1]` | 第一步的可视物，如 a floating terminal window with a command prompt |
| `[STEP_2]` | 第二步，如 a branching task tree on a glass plate |
| `[STEP_3]` | 产出物，如 a glowing wireframe data cube |

## 标题排版

- **中文区**：左侧 35%~45% 留白放 2 行大字标题，关键词用克莱因蓝或亮橙高亮，副标题写交付物（命令/步骤数/版本号）。
- **海外区**：标题压到一行以内的无衬线小标，让图解本身讲故事。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 平面设计 · 等距投影 Isometric | `isometric illustration of smart factory, conveyor belts warehouses delivery trucks stacked in 2.5D, flat colors, technical cutaway` |
| 三维渲染 · 技术线框/蓝图 | `wireframe render, blueprint, technical drawing, blue background, annotations, HUD` |
| 平面设计 · 模块化网格 Modular Grid | `Layout on a strict modular grid, equal square modules, content blocks snapping to grid, clean systematic arrangement, swiss design influence, plenty of white space` |
| 平面设计 · 当代企业极简 Corporate Minimalism | `Modern tech company brand poster, flat minimal design, enormous white space, single bold sans-serif headline, desaturated documentary photography crop, subtle gray, premium clean feel` |

## 避坑

- 不要让 AI 生成大段可读代码或中文小字，界面里的文字一律当纹理处理，真实文字后期叠加。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
