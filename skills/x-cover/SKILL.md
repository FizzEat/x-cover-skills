---
name: x-cover
description: X 长文封面图总入口。根据长文标题/分类/目标区域，从 100 个封面风格 skill 里推荐 3 个最合适的并直接产出提示词。用户说“做个 X 长文封面”“长文头图”“推特文章封面”“封面图提示词”“这篇文章配什么封面”时使用。
---

# X 长文封面路由

基于 X 榜单长文榜 3,917 篇长文、3,535 张封面的分析，把高收藏封面归纳为 11 个视觉家族、100 个可直接调用的风格。

## 怎么选

1. 先判断区域：读者以中文为主 → 优先“中文区优先 / 国内外通用”；面向海外 → 优先“海外区优先 / 国内外通用”。
2. 再判断分类：AI 编程、账号支付、做号变现、AI 创作、财经币圈、职场成长、AI 观察、综合。
3. 最后按文章“承诺”选家族：
   - 承诺**干货/步骤/清单** → A 工科蓝图、I 中文区强文字、E 手绘涂鸦
   - 承诺**结论/数据** → B 研报数据
   - 承诺**认知/哲学/勇气** → C 黑白版画、K 超现实、D 宇宙科幻
   - 承诺**质感/新品** → F 3D 微缩、G 极简编辑
   - 承诺**故事/人** → H 摄影、J 动漫东方
4. 推荐 3 个风格（至少跨 2 个家族），说明各自理由，然后读取对应 `x-cover-<slug>` skill 的模板产出提示词。没有安装对应 skill 时，按下表名称和家族描述直接写。

## 11 个视觉家族

- **A · 工科蓝图与信息结构**：用图解、界面、流程直接展示交付物，是中文区 AI 编程/工具教程的第一大流派。
- **B · 机构研报与数据可视化**：黑底或米白底的研报质感，用一张图表把结论甩在读者脸上，财经币圈与 AI 观察高频使用。
- **C · 黑白版画与哲学隐喻**：海外区收藏量最高的流派。纯黑白、密集点描排线、几乎无字，用一个宏大隐喻承载认知类长文。
- **D · 宇宙科幻与未来视觉**：用尺度和光来表达“范式变化/终局”，适合 AI 观察、行业趋势与宏大叙事。
- **E · 手绘插画与漫画叙事**：用手绘的温度降低阅读门槛，水彩寓言讲商业逻辑，涂鸦流程图讲零基础教程。
- **F · 3D 微缩与商业产品质感**：微距、移轴、黏土、玻璃，用物件的质感制造“高级感”和驻留，适合 AI 产品、模型发布、工具测评。
- **G · 极简编辑与书封海报**：把长文当一本书来包装：杂志封面、经典书封、瑞士海报，靠版式而不是插画取胜。
- **H · 摄影与电影剧照**：真实感照片带来可信度和情绪，适合个人故事、职场成长、生活方式与访谈类长文。
- **I · 中文区强文字转化**：国内长文榜的主力打法：文字占画面 40%~60%，直接展示清单、对比、步骤、收益，贪干货与避坑恐惧双触发。
- **J · 动漫与东方美学**：二次元、国风、日系治愈场景，带来亲和力和收藏欲，适合 AI 创作、个人成长与生活类长文。
- **K · 超现实概念隐喻**：把抽象观点变成一个反常识画面（巨物、错位、门、迷宫），好奇心驱动点击，适合观点与趋势长文。

## 100 个风格速查

| Skill | 名称 | 家族 | 适用分类 | 区域 |
| --- | --- | --- | --- | --- |
| `x-cover-blueprint-isometric` | 白底蓝图等轴测三段流 | A | AI 编程、做号变现、AI 创作 | 中文区优先 |
| `x-cover-terminal-hero` | 暗色终端窗口英雄图 | A | AI 编程、AI 观察 | 国内外通用 |
| `x-cover-node-workflow-window` | 节点工作流软件界面 | A | AI 创作、AI 编程 | 中文区优先 |
| `x-cover-bento-grid` | Bento 便当格功能总览 | A | AI 编程、AI 观察、做号变现 | 国内外通用 |
| `x-cover-swiss-infographic` | 瑞士网格信息图 | A | AI 观察、财经币圈、职场成长 | 国内外通用 |
| `x-cover-checklist-card` | Notion 清单打勾卡 | A | 账号支付、AI 编程、做号变现 | 中文区优先 |
| `x-cover-split-compare` | 左右对比 Before/After | A | AI 编程、AI 创作、职场成长 | 中文区优先 |
| `x-cover-roadmap-timeline` | 路线图时间轴 | A | 职场成长、AI 编程、做号变现 | 国内外通用 |
| `x-cover-architecture-diagram` | 系统架构图海报 | A | AI 编程、AI 观察 | 海外区优先 |
| `x-cover-code-editor-glow` | 代码编辑器光晕 | A | AI 编程 | 海外区优先 |
| `x-cover-black-bar-chart` | 黑底发光柱状图研报 | B | 财经币圈、AI 观察 | 国内外通用 |
| `x-cover-triple-candlestick` | 三联屏 K 线暴涨暴跌 | B | 财经币圈 | 中文区优先 |
| `x-cover-terminal-dashboard` | 彭博终端多面板 | B | 财经币圈、AI 观察 | 海外区优先 |
| `x-cover-heatmap-grid` | 热力图矩阵 | B | 财经币圈、AI 观察 | 海外区优先 |
| `x-cover-big-number-kpi` | 巨型数字 KPI | B | 做号变现、财经币圈、职场成长 | 中文区优先 |
| `x-cover-flow-world-map` | 全球流向地图 | B | 财经币圈、AI 观察、做号变现 | 海外区优先 |
| `x-cover-report-cover-serif` | 卖方研报扉页 | B | 财经币圈、AI 观察 | 海外区优先 |
| `x-cover-newspaper-front` | 报纸头版号外 | B | AI 观察、财经币圈、综合 | 国内外通用 |
| `x-cover-stipple-abyss` | 点描深渊孤舟 | C | 职场成长、综合 | 海外区优先 |
| `x-cover-rocket-ink` | 黑白漫画火箭升空 | C | 职场成长、做号变现 | 海外区优先 |
| `x-cover-dore-engraving` | 多雷式史诗铜版画 | C | AI 观察、综合、职场成长 | 海外区优先 |
| `x-cover-woodcut-bold` | 粗犷木刻版画 | C | 职场成长、综合、做号变现 | 国内外通用 |
| `x-cover-halftone-noir` | 网点黑色电影 | C | 职场成长、AI 观察、综合 | 海外区优先 |
| `x-cover-etching-forest` | 蚀刻迷雾森林 | C | 职场成长、AI 观察 | 海外区优先 |
| `x-cover-mezzotint-portrait` | 美柔汀暗调肖像 | C | 职场成长、综合 | 海外区优先 |
| `x-cover-scratchboard` | 刮板画高光雕刻 | C | AI 观察、综合 | 国内外通用 |
| `x-cover-risograph-duotone` | Riso 孔版双色 | C | 做号变现、AI 创作、综合 | 国内外通用 |
| `x-cover-linocut-nature` | 麻胶版画自然 | C | 职场成长、综合 | 国内外通用 |
| `x-cover-ink-sumi-zen` | 禅意水墨留白 | C | 职场成长、综合 | 国内外通用 |
| `x-cover-cosmic-deity` | 赛博巨神点描 | D | AI 观察、综合 | 海外区优先 |
| `x-cover-retro-space-age` | 复古太空时代海报 | D | AI 观察、AI 编程、综合 | 国内外通用 |
| `x-cover-cyberpunk-neon` | 赛博朋克霓虹街 | D | AI 观察、AI 编程、财经币圈 | 国内外通用 |
| `x-cover-solarpunk-utopia` | 太阳朋克乌托邦 | D | AI 观察、职场成长 | 海外区优先 |
| `x-cover-monolith-desert` | 沙漠黑石碑 | D | AI 观察、综合 | 海外区优先 |
| `x-cover-vaporwave-dream` | 蒸汽波梦境 | D | AI 创作、综合、做号变现 | 国内外通用 |
| `x-cover-newyorker-watercolor` | 纽约客水彩寓言 | E | 财经币圈、做号变现、AI 观察 | 海外区优先 |
| `x-cover-excalidraw-doodle` | Excalidraw 粉彩涂鸦流程 | E | AI 编程、AI 创作、做号变现 | 国内外通用 |
| `x-cover-handdrawn-infographic` | 米白纸手绘信息图 | E | AI 观察、AI 编程、职场成长 | 中文区优先 |
| `x-cover-ligne-claire` | 清线派欧漫 | E | AI 观察、综合、职场成长 | 国内外通用 |
| `x-cover-stick-comic` | 火柴人极简漫画 | E | 职场成长、AI 编程、综合 | 海外区优先 |
| `x-cover-pixel-isometric` | 等轴像素小世界 | E | AI 编程、做号变现、AI 创作 | 国内外通用 |
| `x-cover-gouache-storybook` | 水粉绘本 | E | 职场成长、综合、AI 创作 | 国内外通用 |
| `x-cover-sketchnote-page` | 视觉笔记手账页 | E | 职场成长、AI 观察、做号变现 | 中文区优先 |
| `x-cover-comic-panels` | 美漫分格 | E | AI 观察、综合、做号变现 | 海外区优先 |
| `x-cover-ukiyoe-wave` | 浮世绘大浪 | E | AI 观察、财经币圈、综合 | 国内外通用 |
| `x-cover-apple-macro` | 苹果发布会微距 | F | AI 创作、AI 观察 | 海外区优先 |
| `x-cover-tiltshift-diorama` | 移轴微缩模型 | F | 职场成长、做号变现、AI 观察 | 国内外通用 |
| `x-cover-clay-voxel-character` | 黏土体素小人 | F | AI 创作、AI 编程、做号变现 | 海外区优先 |
| `x-cover-glass-3d-icon` | 玻璃拟态 3D 图标 | F | AI 编程、AI 创作、AI 观察 | 国内外通用 |
| `x-cover-isometric-room` | 3D 等轴小房间 | F | AI 编程、做号变现、职场成长 | 国内外通用 |
| `x-cover-blindbox-figure` | 潮玩盲盒手办 | F | AI 创作、做号变现、综合 | 中文区优先 |
| `x-cover-papercraft-layers` | 纸艺层叠 | F | AI 创作、职场成长、综合 | 国内外通用 |
| `x-cover-brick-build` | 积木搭建 | F | AI 编程、做号变现、职场成长 | 国内外通用 |
| `x-cover-knolling-flatlay` | Knolling 平铺整理 | F | AI 编程、做号变现、AI 创作 | 国内外通用 |
| `x-cover-liquid-chrome` | 液态铬金属 | F | AI 创作、AI 观察 | 海外区优先 |
| `x-cover-kinfolk-serif` | Kinfolk 杂志极简 | G | 职场成长、AI 创作、综合 | 海外区优先 |
| `x-cover-swiss-poster` | 瑞士海报 | G | AI 观察、AI 编程、综合 | 国内外通用 |
| `x-cover-penguin-classic` | 经典平装书封 | G | 职场成长、综合 | 国内外通用 |
| `x-cover-bauhaus-geometry` | 包豪斯几何 | G | AI 观察、AI 编程、综合 | 国内外通用 |
| `x-cover-magazine-cover` | 时代周刊式杂志封面 | G | AI 观察、职场成长、财经币圈 | 海外区优先 |
| `x-cover-type-only` | 纯字体海报底 | G | AI 观察、职场成长、综合 | 中文区优先 |
| `x-cover-japanese-ma` | 日式留白（間） | G | 职场成长、AI 创作、综合 | 国内外通用 |
| `x-cover-neo-brutalism` | 新粗野主义 | G | 做号变现、AI 编程、综合 | 国内外通用 |
| `x-cover-dada-collage` | 达达拼贴 | G | AI 观察、综合、AI 创作 | 国内外通用 |
| `x-cover-constructivist` | 构成主义宣传画 | G | 做号变现、职场成长、AI 观察 | 国内外通用 |
| `x-cover-cinematic-still` | 电影剧照 | H | 职场成长、综合、AI 观察 | 国内外通用 |
| `x-cover-rembrandt-portrait` | 伦勃朗光肖像 | H | 职场成长、综合 | 国内外通用 |
| `x-cover-street-leica` | 徕卡街拍 | H | 职场成长、综合、做号变现 | 海外区优先 |
| `x-cover-portra-film` | Portra 胶片日常 | H | 职场成长、AI 创作、综合 | 国内外通用 |
| `x-cover-desk-flatlay` | 工作台俯拍 | H | AI 编程、做号变现、职场成长 | 国内外通用 |
| `x-cover-documentary-candid` | 纪实抓拍 | H | 做号变现、职场成长、综合 | 中文区优先 |
| `x-cover-golden-silhouette` | 黄金时刻剪影 | H | 职场成长、综合 | 国内外通用 |
| `x-cover-night-long-exposure` | 夜城长曝光 | H | AI 观察、财经币圈、职场成长 | 国内外通用 |
| `x-cover-studio-product-white` | 白底产品棚拍 | H | AI 创作、做号变现、账号支付 | 国内外通用 |
| `x-cover-drone-aerial` | 无人机航拍 | H | AI 观察、职场成长、财经币圈 | 国内外通用 |
| `x-cover-big-claim-poster` | 大字报痛点封面底 | I | 做号变现、账号支付、AI 编程 | 中文区优先 |
| `x-cover-before-after-income` | 收益战报对比 | I | 做号变现、财经币圈 | 中文区优先 |
| `x-cover-three-step-loop` | 三步闭环 | I | AI 编程、做号变现、AI 创作 | 中文区优先 |
| `x-cover-storyboard-grid` | 分镜宫格 | I | AI 创作 | 中文区优先 |
| `x-cover-logo-wall` | 工具矩阵 Logo 墙 | I | AI 编程、AI 创作、做号变现 | 中文区优先 |
| `x-cover-toc-card` | 教程目录卡 | I | AI 编程、AI 创作、职场成长 | 中文区优先 |
| `x-cover-warning-pitfall` | 避坑警示 | I | 账号支付、AI 编程、做号变现 | 中文区优先 |
| `x-cover-qa-bubbles` | 问答对话气泡 | I | AI 观察、职场成长、做号变现 | 中文区优先 |
| `x-cover-screenshot-proof` | 截图证据堆叠 | I | 做号变现、账号支付、AI 编程 | 中文区优先 |
| `x-cover-cheatsheet-table` | 速查表 | I | AI 编程、AI 创作、账号支付 | 中文区优先 |
| `x-cover-anime-sky` | 动画天空背景 | J | 职场成长、AI 创作、综合 | 国内外通用 |
| `x-cover-cozy-anime-room` | 日系治愈书房 | J | 职场成长、AI 创作、综合 | 国内外通用 |
| `x-cover-guochao` | 国潮插画 | J | 做号变现、AI 创作、综合 | 中文区优先 |
| `x-cover-shanshui-ink` | 青绿山水 | J | AI 创作、综合、职场成长 | 国内外通用 |
| `x-cover-wuxia-cinematic` | 武侠电影大片 | J | AI 创作、综合 | 中文区优先 |
| `x-cover-cel-shaded-anime` | 赛璐璐动画角色 | J | AI 创作、做号变现 | 国内外通用 |
| `x-cover-minhwa-folk` | 韩国民画 | J | AI 创作、综合 | 国内外通用 |
| `x-cover-chinese-poster-retro` | 老上海月份牌 | J | 做号变现、财经币圈、综合 | 中文区优先 |
| `x-cover-surreal-scale` | 巨物错位 | K | AI 观察、综合、职场成长 | 海外区优先 |
| `x-cover-double-exposure` | 双重曝光 | K | 职场成长、AI 观察、综合 | 国内外通用 |
| `x-cover-endless-maze` | 无尽迷宫 | K | 职场成长、AI 观察 | 海外区优先 |
| `x-cover-chess-strategy` | 棋局博弈 | K | 财经币圈、AI 观察、职场成长 | 国内外通用 |
| `x-cover-iceberg` | 冰山模型 | K | AI 观察、做号变现、职场成长 | 国内外通用 |
| `x-cover-portal-door` | 旷野中的门 | K | 职场成长、AI 观察、综合 | 国内外通用 |
| `x-cover-mirror-reflection` | 镜中另一个自己 | K | 职场成长、AI 观察 | 海外区优先 |
