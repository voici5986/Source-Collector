#!/usr/bin/env python3
"""download_configs.py - 一键下载所有视频源配置到本地

Usage:
    python scripts/download_configs.py
    python scripts/download_configs.py --app小猫影视
"""

import argparse
import json
import urllib.request
from pathlib import Path

REPOS = {
    "小猫影视": {
        "files": {
            "Sites.json": "https://cdn.jsdelivr.net/gh/cuiocean/ZY-Player-Resources@latest/Sites/Sites.json",
            "yoyo.json": "https://cdn.jsdelivr.net/gh/waifu-project/v1@latest/yoyo.json",
        }
    },
    "LibreTV/MoonTV": {
        "files": {
            "config_isadult.json": None,  # 本地已有
            "configplus_isadult.json": None,
        }
    },
    "OmniBox": {
        "files": {
            "sites_export.json": "https://cdn.jsdelivr.net/gh/adminlove520/Source-Collector@sites_export_2025-09-29.json",
        }
    },
    "DecoTV/LunaTV": {
        "files": {
            "source.json": "https://cdn.jsdelivr.net/gh/adminlove520/Source-Collector@sources-2025.11.20.json",
        }
    },
}


def download_file(url: str, dest: Path) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            content = resp.read()
        dest.write_bytes(content)
        print(f"  ✅ {dest.name} ({len(content):,} bytes)")
        return True
    except Exception as e:
        print(f"  ❌ {dest.name}: {e}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="下载视频源配置文件")
    parser.add_argument("--app", choices=list(REPOS.keys()), help="仅下载指定应用配置")
    parser.add_argument("--outdir", default="downloads", help="输出目录（默认：downloads）")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(exist_ok=True)

    apps = [args.app] if args.app else list(REPOS.keys())

    print(f"📦 下载视频源配置到 {outdir.absolute()}\n")
    for app_name in apps:
        info = REPOS[app_name]
        print(f"[{app_name}]")
        for fname, url in info["files"].items():
            dest = outdir / fname
            if url:
                download_file(url, dest)
            else:
                # 从本仓库复制
                src = Path(__file__).parent.parent / fname
                if src.exists():
                    dest.write_bytes(src.read_bytes())
                    print(f"  📁 {dest.name} (已从本地复制)")
                else:
                    print(f"  ⚠️  {dest.name}: 本地文件不存在")

    print(f"\n完成！配置文件保存在 {outdir.absolute()}")


if __name__ == "__main__":
    main()
