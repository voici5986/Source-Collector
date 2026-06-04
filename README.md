# 📺 Source-Collector

> 视频源收集器 — 收集整理适用于各类影视应用的 JSON 配置文件，支持小猫影视 / LibreTV / OmniBox / DecoTV / LunaTV

[![GitHub stars](https://img.shields.io/github/stars/adminlove520/Source-Collector)](https://github.com/adminlove520/Source-Collector/stargazers)
[![自动更新](https://img.shields.io/badge/自动更新-每日%2023:00-4caf50)](.github/workflows/auto-update-video-sources.yml)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## ⚠️ 免责声明

- 本项目仅供学习和个人使用，为避免版权纠纷，请严格遵守相关法律法规
- **请勿**在 B站、小红书、微信公众号、抖音、今日头条等中国大陆社交平台发布相关内容
- 不授权任何"科技周刊/月刊"类项目或站点收录本项目

---

## 🌟 功能特性

- **一站式覆盖**：同时收录 LibreTV、MoonTV、小猫影视、OmniBox、DecoTV、LunaTV 等多款影视应用配置
- **自动更新**：GitHub Actions 每日 23:00 自动从上游拉取最新配置，确保始终可用
- **脚本工具**：提供 JSON 验证脚本和配置下载工具
- **Issue 贡献**：支持 GitHub Issue 提交视频源，自动处理 PR

---

## 📁 配置文件说明

| 文件 | 适用应用 | 视频源数 | 自动更新 |
|------|---------|---------|---------|
| `Sites.json` | 小猫影视 / Movie | ~ | ✅ jsdelivr CDN |
| `yoyo.json` | 小猫影视 / Movie | ~ | ✅ jsdelivr CDN |
| `config_isadult.json` | LibreTV / MoonTV | ~ | ❌ 手动维护 |
| `configplus_isadult.json` | LibreTV / MoonTV (Plus) | ~ | ❌ 手动维护 |
| `sites_export_2025-09-29.json` | OmniBox v1.2.7+ | ~ | ❌ |
| `source-2025.11.20.json` | DecoTV / LunaTV | 46 | ❌ |

> **注意**：小猫影视已闭源，相关配置文件可能出现异常，正在评估替代方案。

---

## 🚀 快速使用

### 方式一：直接下载

```bash
# 下载所有配置
python scripts/download_configs.py

# 下载指定应用配置
python scripts/download_configs.py --app 小猫影视 --outdir ~/movie-sources
```

### 方式二：从 CDN 引用（懒加载）

```javascript
// JavaScript 示例：懒加载视频源
const res = await fetch('https://cdn.jsdelivr.net/gh/adminlove520/Source-Collector@latest/yoyo.json');
const sources = await res.json();
```

### 方式三：GitHub Raw 链接

```
https://raw.githubusercontent.com/adminlove520/Source-Collector/main/yoyo.json
```

---

## 🔍 验证配置文件

```bash
# 验证所有 JSON 格式和字段完整性
python scripts/validate_sources.py

# 输出示例：
# 检查 6 个配置文件...
# ✅ Sites.json (小猫影视 / Movie) — 45 个视频源
# ✅ yoyo.json (小猫影视 / Movie) — 38 个视频源
# ❌ config_isadult.json — JSON 解析错误
```

---

## 🛠️ 贡献视频源

### 通过 GitHub Issue 提交（推荐）

1. 进入 [新建 Issue](https://github.com/adminlove520/Source-Collector/issues/new/choose)
2. 选择「视频源提交」模板
3. 填写 JSON 格式的视频源数据
4. 提交后系统自动验证并生成 PR

### JSON 格式要求

```json
{
  "name": "源名称（必需）",
  "api": "https://example.com/api（必需）",
  "key": "标识符（可选）",
  "detail": "详情页 URL（可选）",
  "group": "分组（可选）",
  "disabled": false,
  "is_adult": false
}
```

### 通过 GitHub Actions 自动处理流程

```
提交 Issue → 自动验证 JSON → 提取信息 → 更新 README → 生成 PR → 回复结果
```

---

## 🏗️ 本地开发

```bash
# 克隆仓库
git clone https://github.com/adminlove520/Source-Collector.git
cd Source-Collector

# 安装验证工具依赖（仅需标准库，无需额外依赖）
python scripts/validate_sources.py   # 验证所有配置

# 下载配置到本地
python scripts/download_configs.py --outdir ./my-sources
```

---

## 📂 目录结构

```
Source-Collector/
├── .github/
│   ├── ISSUE_TEMPLATE/          # Issue 模板
│   └── workflows/
│       ├── auto-update-video-sources.yml   # 每日自动更新
│       └── process-video-sources.yml        # Issue 提交处理
├── scripts/
│   ├── validate_sources.py     # JSON 验证工具
│   └── download_configs.py      # 配置下载工具
├── Sites.json                   # 小猫影视
├── yoyo.json                    # 小猫影视
├── config_isadult.json          # LibreTV / MoonTV
├── configplus_isadult.json      # LibreTV / MoonTV (Plus)
├── sites_export_2025-09-29.json # OmniBox
└── README.md
```

---

## 🤝 鸣谢

- [LibreTV](https://github.com/LibreSpark/LibreTV)
- [MoonTV](https://github.com/samqin123/MoonTV)
- [小猫影视](https://github.com/waifu-project/movie)
- [DecoTV](https://github.com/Decohererk/DecoTV)
- [LunaTV](https://github.com/SzeMeng76/LunaTV)

---

## 📝 License

MIT License · adminlove520
