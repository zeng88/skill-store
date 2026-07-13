import tempfile
import unittest
from pathlib import Path

from scripts.gen_download_links import build_download_list


class DownloadListTest(unittest.TestCase):
    """验证下载清单的分类、排序和链接生成规则。"""

    def test_builds_sorted_raw_and_cdn_links(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skills_dir = Path(directory)
            (skills_dir / "z_category").mkdir()
            (skills_dir / "a_category").mkdir()
            (skills_dir / "z_category" / "later.zip").write_bytes(b"zip")
            (skills_dir / "a_category" / "first.zip").write_bytes(b"zip")
            (skills_dir / "a_category" / "ignore.txt").write_text("忽略", encoding="utf-8")

            content = build_download_list(skills_dir, "demo/skill-store", "main")

            self.assertIn("共 **2** 个 Skill 压缩包。", content)
            self.assertLess(content.index("## a_category"), content.index("## z_category"))
            self.assertIn(
                "https://raw.githubusercontent.com/demo/skill-store/main/skills/a_category/first.zip",
                content,
            )
            self.assertIn(
                "https://cdn.jsdelivr.net/gh/demo/skill-store@main/skills/z_category/later.zip",
                content,
            )
            self.assertNotIn("ignore.txt", content)


if __name__ == "__main__":
    unittest.main()
