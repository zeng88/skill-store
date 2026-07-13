# Agnes Video Skill

## 用途

该压缩包封装 Agnes Video V2.0 能力，支持文生视频、图生视频、自定义时长、自动下载、任务日志、任务状态查询和超时后的下载恢复。

## 包内主要文件

- `SKILL.md`：供 Agent 加载的 Skill 定义。
- `scripts/agnes_video.py`：核心命令行脚本。
- `references/api.md`：接口参考。
- `docs/implementation-plan.md`：实现方案记录。

## 依赖与配置

- Python 3.8 及以上。
- 仅使用 Python 标准库；如遇 macOS SSL 证书问题，可按包内 README 安装 `certifi`。
- 调用前设置 `AGNES_API_KEY`；也兼容 `AGNES_API_TOKEN` 和 `APIHUB_AGNES_API_KEY`。

## 调用示例

解压后可按包内 README 执行：

```bash
export AGNES_API_KEY="sk-your-key-here"
python3 agnes-video-skill/scripts/agnes_video.py generate \
  --prompt "镜头缓慢推进一片晨雾中的森林" \
  --download
```

任务恢复和状态查询：

```bash
python3 agnes-video-skill/scripts/agnes_video.py status --task-id TASK_ID
python3 agnes-video-skill/scripts/agnes_video.py recover
```

## 文件校验

- 文件：`skills/ai_media/agnes-video-skill.zip`
- SHA-256：`cc4449b5cf3c369c5c5ed47d4634127d84836094c4ab22b38a73a9d647e031d1`
