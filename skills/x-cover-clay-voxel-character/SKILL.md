---
name: x-cover-clay-voxel-character
description: X 长文封面图：黏土体素小人（3D 微缩与商业产品质感）。海外 AI 创作第一同款：可爱的小方块人举着 App 图标奔跑。 适用 AI 创作、AI 编程、做号变现 类长文，海外区优先。用户要做 X/推特长文封面、文章头图、公众号封面并想要“黏土体素小人”风格时使用。
---

# 黏土体素小人

> 海外 AI 创作第一同款：可爱的小方块人举着 App 图标奔跑。

| 项 | 内容 |
| --- | --- |
| 视觉家族 | F · 3D 微缩与商业产品质感 |
| 适用分类 | AI 创作、AI 编程、做号变现 |
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

- **Identity 身份**：北欧极简设计厂牌封面
- **Spatial 空间**：中心对称，大量留白
- **Visual State 终端视觉状态**：黏土小方块角色奔跑着举起 [ICON]
- **Material 材质响应**：哑光黏土，羊皮纸底 #FAF8F5
- **Lighting 光学**：漫射柔光，脚下胶囊投影

## 提示词模板

```text
Ultra-minimalist graphic design cover, warm cream parchment background (#FAF8F5). Centered: a cute tiny rectangular clay voxel character running joyfully, holding up [ICON]. Generous empty space below for an elegant serif title. Scandinavian minimalism, Kinfolk magazine style, soft ambient occlusion, tactile matte texture, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
| `[ICON]` | 举着的东西，如 a sleek violet rounded app icon with a white sine wave |

## 标题排版

- **中文区**：主体放画面中心或右侧 1/3，标题放留白一侧，字色取主体主色。
- **海外区**：一行优雅衬线或 SF 风格无衬线，大量留白。

## 风格增强词

从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：

| 灵感台卡片 | 英文关键词 |
| --- | --- |
| 动画 · 定格黏土（Claymation） | `claymation stop-motion, Plasticine characters, fingerprint and tool marks, soft squishy deformation, matte finish, Aardman comedy timing` |
| 三维渲染 · 体素 | `voxel art, cubic blocks, MagicaVoxel style, pixel 3D, blocky, minecraft` |
| 三维渲染 · 极简主义 | `minimalist, clean composition, negative space, monochrome palette, simple geometry` |
| 平面设计 · 大留白 Generous Whitespace | `Luxury minimal poster, 90 percent empty white space, single small black typographic element in lower third, extreme restraint, premium gallery feel, no decoration` |
| 动画 · Aardman 黏土喜剧节奏 | `Aardman clay comedy, visible fingerprint clay texture, British deadpan humor, exaggerated lip-sync, wool sweater knit texture, Nick Park, Wallace and Gromit` |
| 三维渲染 · 体素化建模雕刻 | `voxel modeling, MagicaVoxel, blocky voxels, pixel art 3D` |

## 避坑

- 不要出现真实品牌 Logo 和商标外形，用“a sleek violet app icon”这类泛化描述代替。
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
