#!/usr/bin/env python3
"""validate_sources.py - 验证所有视频源 JSON 配置文件格式"""

import json
import sys
from pathlib import Path

FIELDS_REQUIRED = {"name", "api"}
FIELDS_OPTIONAL = {"key", "detail", "disabled", "is_adult", "group", "id", "download", "jiexiUrl", "reverseOrder"}

SUPPORTED_APPS = {
    "Sites.json": "小猫影视 / Movie",
    "yoyo.json": "小猫影视 / Movie",
    "config_isadult.json": "LibreTV / MoonTV",
    "configplus_isadult.json": "LibreTV / MoonTV (Plus)",
    "sites_export_2025-09-29.json": "OmniBox",
    "video_sources_2025-11-19T09-22-39.json": "DecoTV / LunaTV",
    "source-2025.11.20.json": "DecoTV / LunaTV",
}


def validate_file(filepath: Path) -> tuple[bool, list[str]]:
    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"JSON 解析错误: {e}"]

    items = data if isinstance(data, list) else data.get("data", [])
    if not isinstance(items, list):
        return False, [f"期望 JSON 数组，实际类型: {type(items).__name__}"]

    for i, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"  [{i}] 不是对象: {type(item).__name__}")
            continue

        missing = FIELDS_REQUIRED - item.keys()
        if missing:
            errors.append(f"  [{i}] 缺少必需字段: {missing} (name={item.get('name', '?')})")

        extra = item.keys() - FIELDS_REQUIRED - FIELDS_OPTIONAL
        if extra:
            errors.append(f"  [{i}] 未知字段: {extra} (name={item.get('name', '?')})")

        if "api" in item and not item["api"].startswith(("http://", "https://")):
            errors.append(f"  [{i}] API 不是有效 URL: {item['api']} (name={item.get('name', '?')})")

    return not errors, errors


def main() -> None:
    repo_root = Path(__file__).parent.parent
    json_files = [f for f in repo_root.iterdir() if f.suffix == ".json" and f.name in SUPPORTED_APPS]

    if not json_files:
        print("未找到任何已知的视频源配置文件。")
        sys.exit(1)

    print(f"检查 {len(json_files)} 个配置文件...\n")
    all_ok = True
    results = []

    for fp in sorted(json_files):
        ok, errors = validate_file(fp)
        app = SUPPORTED_APPS.get(fp.name, "未知")
        items = []
        try:
            with open(fp, encoding="utf-8") as f:
                data = json.load(f)
                items = data if isinstance(data, list) else data.get("data", [])
        except Exception:
            pass

        status = "✅" if ok else "❌"
        results.append((ok, fp.name, app, len(items), errors))
        if not ok:
            all_ok = False

    for ok, name, app, count, errors in results:
        status = "✅" if ok else "❌"
        print(f"{status} {name} ({app}) — {count} 个视频源")
        for e in errors:
            print(f"   {e}")

    print()
    if all_ok:
        print(f"全部 {len(json_files)} 个配置文件验证通过 ✅")
    else:
        print("部分配置文件存在问题，请修复后提交 ❌")
        sys.exit(1)


if __name__ == "__main__":
    main()
