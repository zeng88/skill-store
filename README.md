# Skill Store

本仓库统一收纳可独立分发的 AI Agent Skill 压缩包（`.zip`）。每个 Skill 独立打包、互不耦合，支持按分类浏览、单文件下载和批量获取。

## 当前技能

| 分类 | Skill | 说明 | 下载 |
| --- | --- | --- | --- |
| `ai_media` | Agnes Image Skill | 文生图、图生图、多参考图与本地下载 | [Raw](https://raw.githubusercontent.com/zeng88/skill-store/main/skills/ai_media/agnes-image-skill.zip) / [jsDelivr](https://cdn.jsdelivr.net/gh/zeng88/skill-store@main/skills/ai_media/agnes-image-skill.zip) |
| `ai_media` | Agnes Video Skill | 文生视频、图生视频、任务恢复与本地下载 | [Raw](https://raw.githubusercontent.com/zeng88/skill-store/main/skills/ai_media/agnes-video-skill.zip) / [jsDelivr](https://cdn.jsdelivr.net/gh/zeng88/skill-store@main/skills/ai_media/agnes-video-skill.zip) |

更多文件见[完整下载清单](download_list.md)。

## 仓库结构

```text
skill-store/
├── README.md
├── docs/                    # Skill 配套说明
│   └── ai_media/
├── scripts/                 # 清单生成等辅助脚本
├── skills/                  # 所有独立 Skill 压缩包
│   └── ai_media/
├── tests/                   # 脚本测试
└── download_list.md         # 自动生成的下载清单
```

## 下载单个 Skill

### 浏览器下载

打开目标 `.zip` 的 Raw 链接即可下载。国内网络环境可优先使用 jsDelivr 链接。

### curl / wget

```bash
curl -fL -o agnes-image-skill.zip \
  "https://cdn.jsdelivr.net/gh/zeng88/skill-store@main/skills/ai_media/agnes-image-skill.zip"

wget -O agnes-video-skill.zip \
  "https://raw.githubusercontent.com/zeng88/skill-store/main/skills/ai_media/agnes-video-skill.zip"
```

### Python

```python
from pathlib import Path
from urllib.request import urlopen

url = "https://raw.githubusercontent.com/zeng88/skill-store/main/skills/ai_media/agnes-image-skill.zip"
with urlopen(url, timeout=60) as response:
    Path("agnes-image-skill.zip").write_bytes(response.read())
```

## 完整获取仓库

```bash
git clone https://github.com/zeng88/skill-store.git
```

## 新增 Skill

1. 在 `skills/` 下按业务建立分类目录，并放入独立 `.zip` 文件。
2. 在 `docs/对应分类/` 下补充用途、依赖、配置参数和调用示例。
3. 单包建议小于 100 MB；更大的资源应拆分或作为 GitHub Release 附件发布。
4. 文件名建议使用 `{功能名称}_{版本}.zip`，例如 `pdf_extract_v1.2.zip`。
5. 执行 `python3 scripts/gen_download_links.py` 更新下载清单。
6. 检查变更后再提交 Pull Request。

## 生成下载清单

脚本会递归扫描 `skills/` 下的 `.zip`，按分类排序并生成 Raw 与 jsDelivr 下载地址：

```bash
python3 scripts/gen_download_links.py
```

可显式指定仓库和分支，便于迁移到其他 GitHub 仓库：

```bash
python3 scripts/gen_download_links.py \
  --repo your-name/skill-zip-store \
  --branch main
```

也可以用 `SKILL_STORE_REPO` 和 `SKILL_STORE_BRANCH` 环境变量设置默认值。

## 约束与注意事项

- Raw 和 CDN 链接依赖 GitHub 分支及路径大小写，下载 404 时请先核对二者。
- 不要将 API Key、密码、私有配置或个人隐私文件打包进 Skill。
- 修改或删除 `.zip` 后必须重新生成 `download_list.md`。
- GitHub 单文件限制为 100 MB；生产环境建议使用带版本号的 Releases 管理正式发布包。

## 目录文档

- [Agnes Image Skill](docs/ai_media/agnes-image-skill.md)
- [Agnes Video Skill](docs/ai_media/agnes-video-skill.md)
