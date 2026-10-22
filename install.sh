#!/usr/bin/env bash
# 安装 X 长文封面 skill
#   ./install.sh                       只装路由 skill x-cover
#   ./install.sh --family A,C,I        路由 + 指定家族
#   ./install.sh --all                 全部 101 个
#   ./install.sh --target DIR ...      自定义安装目录（默认 ~/.claude/skills）
set -euo pipefail

cd "$(dirname "$0")"
TARGET="$HOME/.claude/skills"
FAMILY=""
ALL=0

while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --family) FAMILY="$2"; shift 2 ;;
    --all) ALL=1; shift ;;
    *) echo "未知参数: $1"; exit 1 ;;
  esac
done

mkdir -p "$TARGET"
picked=("x-cover")
if [ "$ALL" = 1 ]; then
  for d in skills/x-cover-*; do picked+=("$(basename "$d")"); done
elif [ -n "$FAMILY" ]; then
  while IFS= read -r s; do picked+=("$s"); done < <(
    python3 -c "import json,sys;fs=set(sys.argv[1].upper().split(','));print('\n'.join(x['skill'] for x in json.load(open('catalog.json')) if x['family'] in fs))" "$FAMILY")
fi

for s in "${picked[@]}"; do
  rm -rf "$TARGET/$s"
  cp -R "skills/$s" "$TARGET/$s"
done
echo "已安装 ${#picked[@]} 个 skill 到 $TARGET"
