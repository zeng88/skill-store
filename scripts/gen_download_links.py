#!/usr/bin/env python3
"""生成 Skill Store 的单文件下载清单。

脚本只依赖 Python 标准库，适合在提交前或 CI 中运行。
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path
from urllib.parse import quote


DEFAULT_REPO = "zeng88/skill-store"
DEFAULT_BRANCH = "main"


def detect_github_repo(root: Path) -> str | None:
    """从 origin 远程地址提取 GitHub 的 owner/repository。"""
    try:
        remote = subprocess.check_output(
            ["git", "-C", str(root), "config", "--get", "remote.origin.url"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return None

    match = re.search(r"github\.com[/:]([^/]+/[^/]+?)(?:\.git)?$", remote)
    return match.group(1) if match else None


def build_download_list(skills_dir: Path, repo: str, branch: str) -> str:
    """扫描压缩包并返回稳定、可重复生成的 Markdown 内容。"""
    zip_files = sorted(
        (path for path in skills_dir.rglob("*") if path.is_file() and path.suffix.lower() == ".zip"),
        key=lambda path: path.relative_to(skills_dir).as_posix().lower(),
    )

    grouped: dict[str, list[Path]] = {}
    for zip_file in zip_files:
        relative = zip_file.relative_to(skills_dir)
        category = "/".join(relative.parts[:-1]) or "未分类"
        grouped.setdefault(category, []).append(relative)

    lines = [
        "# 全部技能下载清单",
        "",
        "> 本文件由 `scripts/gen_download_links.py` 自动生成，请勿手工编辑。",
        "> 每个条目同时提供 GitHub Raw 和 jsDelivr CDN 地址。",
        "",
        f"共 **{len(zip_files)}** 个 Skill 压缩包。",
        "",
    ]

    if not zip_files:
        lines.append("当前 `skills/` 下暂无 `.zip` 文件。")
        return "\n".join(lines) + "\n"

    for category, relative_files in sorted(grouped.items(), key=lambda item: item[0].lower()):
        lines.extend([f"## {category}", ""])
        for relative in relative_files:
            encoded_path = "/".join(quote(part) for part in relative.parts)
            raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/skills/{encoded_path}"
            cdn_url = f"https://cdn.jsdelivr.net/gh/{repo}@{branch}/skills/{encoded_path}"
            lines.append(
                f"- `{relative.name}`：[Raw 下载]({raw_url}) · [jsDelivr 加速]({cdn_url})"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    """解析命令行参数，并保留迁移仓库时的可配置性。"""
    parser = argparse.ArgumentParser(description="生成 Skill Store 下载链接清单")
    parser.add_argument("--repo", help="GitHub 仓库，格式为 owner/repository")
    parser.add_argument("--branch", help="GitHub 分支名，默认 main")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="仓库根目录，默认取当前脚本所在仓库",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="输出文件，默认写入仓库根目录的 download_list.md",
    )
    return parser.parse_args()


def main() -> int:
    """执行生成流程并写入 UTF-8 文件。"""
    args = parse_args()
    root = args.root.resolve()
    repo = args.repo or os.getenv("SKILL_STORE_REPO") or detect_github_repo(root) or DEFAULT_REPO
    branch = args.branch or os.getenv("SKILL_STORE_BRANCH") or DEFAULT_BRANCH

    if not re.fullmatch(r"[^/\s]+/[^/\s]+", repo):
        raise SystemExit("错误：--repo 必须使用 owner/repository 格式")
    if not branch.strip():
        raise SystemExit("错误：分支名不能为空")

    output = (args.output or root / "download_list.md").resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    content = build_download_list(root / "skills", repo, branch)
    output.write_text(content, encoding="utf-8")
    print(f"已生成 {output}：共 {content.count(' · [jsDelivr 加速]')} 个 Skill 压缩包")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
