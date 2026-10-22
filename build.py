"""生成 100 个 X 长文封面 skill。

用法:
  python3 build.py                       # 用仓库内 data/enrich.json 生成
  python3 build.py --lingan /path/data.js # 从 AIGC 灵感台重新抽取风格增强词后生成

产出: skills/x-cover-*/SKILL.md、skills/x-cover/SKILL.md(路由)、catalog.json、CATALOG.md、README 目录段
"""
import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "specs"))
from families import FAMILIES  # noqa: E402
from skills import SKILLS  # noqa: E402

ZONE = {"cn": "中文区优先", "gl": "海外区优先", "both": "国内外通用"}
PGVP_KEYS = ["Identity 身份", "Spatial 空间", "Visual State 终端视觉状态", "Material 材质响应", "Lighting 光学"]
ENRICH_PATH = ROOT / "data" / "enrich.json"
PER_SKILL = 6


def load_lingan(path):
    """用 node 读取灵感台 data.js，只保留带英文关键词的风格卡。"""
    js = f"global.window={{}};require({json.dumps(str(path))});" \
         "process.stdout.write(JSON.stringify(window.DATA.cards))"
    cards = json.loads(subprocess.check_output(["node", "-e", js]))
    out = []
    for c in cards:
        en = c.get("en") or ""
        if not en or len(en) > 220:
            continue
        f = c.get("f") or {}
        feat = f.get("视觉特征") or f.get("特征") or f.get("说明") or ""
        out.append({"lib": c["lib"], "axis": c["axis"], "name": c["name"], "en": en, "feat": feat[:60]})
    return out


def match(cards, terms):
    """按检索词轮询匹配，每个词轮流取一张，凑满 PER_SKILL 张。"""
    buckets = []
    for t in terms:
        t = t.strip().lower()
        if t:
            buckets.append([c for c in cards if t in c["name"].lower() or t in c["axis"].lower()])
    picked, seen = [], set()
    while len(picked) < PER_SKILL and any(buckets):
        for b in buckets:
            while b:
                c = b.pop(0)
                if c["name"] not in seen:
                    seen.add(c["name"])
                    picked.append(c)
                    break
            if len(picked) >= PER_SKILL:
                break
    return picked


def parse_vars(s):
    return [tuple(x.split("=", 1)) for x in s.split(";") if "=" in x]


def render_skill(sk):
    fam = FAMILIES[sk["fam"]]
    slug = f"x-cover-{sk['slug']}"
    cats = "、".join(sk["cats"])
    desc = (f"X 长文封面图：{sk['name']}（{fam['name']}）。{sk['hook']} "
            f"适用 {cats} 类长文，{ZONE[sk['zone']]}。用户要做 X/推特长文封面、文章头图、"
            f"公众号封面并想要“{sk['name']}”风格时使用。")
    pgvp = "\n".join(f"- **{k}**：{v}" for k, v in zip(PGVP_KEYS, sk["pgvp"]))
    vars_ = "\n".join(f"| `[{k}]` | {v} |" for k, v in parse_vars(sk["vars"]))
    enrich = sk.get("enrich") or []
    if enrich:
        rows = "\n".join(f"| {c['lib']} · {c['name']} | `{c['en']}` |" for c in enrich)
        enrich_md = ("从 AIGC 灵感台匹配到的可叠加风格词，挑 1~2 条追加到提示词末尾即可微调质感：\n\n"
                     "| 灵感台卡片 | 英文关键词 |\n| --- | --- |\n" + rows)
    else:
        enrich_md = "（灵感台暂无匹配卡片，直接使用模板即可。）"
    tpl = sk["tpl"].strip()
    return slug, desc, f"""---
name: {slug}
description: {desc}
---

# {sk['name']}

> {sk['hook']}

| 项 | 内容 |
| --- | --- |
| 视觉家族 | {sk['fam']} · {fam['name']} |
| 适用分类 | {cats} |
| 区域倾向 | {ZONE[sk['zone']]} |
| 推荐画幅 | 16:9 出图，上传 X 长文前裁成 5:2，主体放中间 60% 安全区 |

## 工作流

1. 读用户给的长文标题、摘要或正文，提炼一句话核心观点和目标读者。
2. 把观点翻译成本风格能承载的画面：按下方“变量”逐个填空，变量必须是具体的可见物体，不写抽象词。
3. 输出 3 个版本：**稳妥版**（贴近模板）、**强钩子版**（放大冲突或尺度）、**反差版**（换一个意料之外的主体）。
4. 每个版本给出：中文画面说明一句 + 完整英文提示词 + 标题排版建议。
5. 按用户使用的模型补参数：Midjourney 末尾加 `--ar 16:9 --style raw`；FLUX / GPT-Image / Imagen 直接用自然语言并在开头写 `16:9 landscape`；即梦/豆包可把提示词翻成中文。
6. 提醒用户：画面里的文字一律后期排版，AI 只负责底图。

## PGVP 结构拆解

{pgvp}

## 提示词模板

```text
{tpl}, 16:9 landscape --ar 16:9
```

| 变量 | 怎么填 |
| --- | --- |
{vars_}

## 标题排版

- **中文区**：{fam['title_cn']}
- **海外区**：{fam['title_gl']}

## 风格增强词

{enrich_md}

## 避坑

- {fam['avoid']}
- 不要要求画面出现真实品牌 Logo、商标或真人肖像，不写在世艺术家姓名；胶片型号、杂志名这类风格参照词可以保留。
- 一次只改一个变量做对比，方便判断是哪个词起作用。
"""


def render_router(skills):
    rows = "\n".join(
        f"| `x-cover-{s['slug']}` | {s['name']} | {s['fam']} | {'、'.join(s['cats'])} | {ZONE[s['zone']]} |"
        for s in skills)
    fams = "\n".join(f"- **{k} · {v['name']}**：{v['desc']}" for k, v in FAMILIES.items())
    return f"""---
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

{fams}

## 100 个风格速查

| Skill | 名称 | 家族 | 适用分类 | 区域 |
| --- | --- | --- | --- | --- |
{rows}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lingan", help="AIGC 灵感台 data.js 路径，提供则重新抽取风格增强词")
    args = ap.parse_args()

    if args.lingan:
        cards = load_lingan(args.lingan)
        enrich = {s["slug"]: match(cards, s["terms"]) for s in SKILLS}
        ENRICH_PATH.parent.mkdir(exist_ok=True)
        ENRICH_PATH.write_text(json.dumps(enrich, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"灵感台卡片 {len(cards)} 张，已写入 {ENRICH_PATH.relative_to(ROOT)}")
    enrich = json.loads(ENRICH_PATH.read_text(encoding="utf-8")) if ENRICH_PATH.exists() else {}

    out = ROOT / "skills"
    if out.exists():
        shutil.rmtree(out)
    catalog = []
    for s in SKILLS:
        s["enrich"] = enrich.get(s["slug"], [])
        slug, desc, md = render_skill(s)
        (out / slug).mkdir(parents=True)
        (out / slug / "SKILL.md").write_text(md, encoding="utf-8")
        catalog.append({"skill": slug, "name": s["name"], "family": s["fam"],
                        "family_name": FAMILIES[s["fam"]]["name"], "categories": s["cats"],
                        "zone": s["zone"], "hook": s["hook"],
                        "prompt_template": s["tpl"], "variables": dict(parse_vars(s["vars"]))})
    (out / "x-cover").mkdir()
    (out / "x-cover" / "SKILL.md").write_text(render_router(SKILLS), encoding="utf-8")
    (ROOT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=1), encoding="utf-8")

    lines = ["# 100 个封面风格目录\n"]
    for k, v in FAMILIES.items():
        group = [s for s in SKILLS if s["fam"] == k]
        lines.append(f"\n## {k} · {v['name']}（{len(group)}）\n\n{v['desc']}\n")
        lines.append("| Skill | 名称 | 一句话 | 适用分类 | 区域 |\n| --- | --- | --- | --- | --- |")
        lines += [f"| [`x-cover-{s['slug']}`](skills/x-cover-{s['slug']}/SKILL.md) | {s['name']} | {s['hook']} "
                  f"| {'、'.join(s['cats'])} | {ZONE[s['zone']]} |" for s in group]
    (ROOT / "CATALOG.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    readme = ROOT / "README.md"
    if readme.exists():
        summary = "\n".join(f"| {k} | {v['name']} | {sum(1 for s in SKILLS if s['fam'] == k)} | {v['desc']} |"
                            for k, v in FAMILIES.items())
        block = "| 家族 | 名称 | 数量 | 说明 |\n| --- | --- | --- | --- |\n" + summary
        text = readme.read_text(encoding="utf-8")
        text = re.sub(r"<!-- FAMILIES:START -->.*<!-- FAMILIES:END -->",
                      f"<!-- FAMILIES:START -->\n{block}\n<!-- FAMILIES:END -->", text, flags=re.S)
        readme.write_text(text, encoding="utf-8")
    print(f"生成 {len(SKILLS)} 个风格 skill + 1 个路由 skill")


if __name__ == "__main__":
    main()
