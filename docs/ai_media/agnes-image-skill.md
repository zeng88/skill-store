# Agnes Image Skill

## 用途

该压缩包封装 Agnes 图片生成能力，支持文生图、图生图、本地或 URL 参考图、多参考图、中文提示词翻译、结果下载和 `seed` 复现控制。

## 包内主要文件

- `SKILL.md`：供 Agent 加载的 Skill 定义。
- `scripts/agnes_image.py`：命令行调用脚本。
- `references/api.md`：接口参考。

## 依赖与配置

- Python 3.8 及以上。
- 仅使用 Python 标准库，无需额外安装依赖。
- 调用前设置 `AGNES_API_KEY`；也兼容 `AGNES_API_TOKEN` 和 `APIHUB_AGNES_API_KEY`。

## 调用示例

解压后可按包内 README 执行：

```bash
export AGNES_API_KEY="sk-your-key-here"
python3 agnes-image-skill/scripts/agnes_image.py --prompt "一只在月光下的猫"
```

本地参考图和自动下载示例：

```bash
python3 agnes-image-skill/scripts/agnes_image.py \
  --prompt "把背景改成森林" \
  --image ./input.png \
  --download
```

## 文件校验

- 文件：`skills/ai_media/agnes-image-skill.zip`
- SHA-256：`5c33d5e4a67c21623a5a6ff27c8bba192c23e7da918aae6eb14218be74df679c`
