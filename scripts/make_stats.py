"""从抓取的长文元数据生成聚合统计（不含正文摘要和图片，只保留标题/作者/收藏数）。

用法: python3 scripts/make_stats.py /path/to/articles_data.json
输出: data/stats.json
"""
import collections
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

def main(src):
    rows = json.load(open(src, encoding="utf-8"))
    total = collections.Counter()
    covers = collections.Counter()
    top = collections.defaultdict(list)
    for r in rows:
        key = f"{r['zone']}|{r['cat_name']}"
        total[key] += 1
        if r.get("img_url"):
            covers[key] += 1
        top[key].append({"title": r["title"], "author": r["author_name"],
                         "handle": r["author_handle"], "fav": r["fav"]})
    out = {
        "source": "https://xbangdan.com/articles/",
        "articles": len(rows),
        "covers": sum(covers.values()),
        "by_zone_category": [
            {"zone": k.split("|")[0], "category": k.split("|")[1],
             "articles": total[k], "covers": covers[k],
             "top5": sorted(top[k], key=lambda x: -x["fav"])[:5]}
            for k in sorted(total, key=lambda k: -covers[k])
        ],
    }
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "stats.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1)
        .replace("\u3010", "（").replace("\u3011", "）"), encoding="utf-8")
    print(out["articles"], out["covers"])

if __name__ == "__main__":
    main(sys.argv[1])
