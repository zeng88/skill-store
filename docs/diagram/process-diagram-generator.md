# Process Diagram Generator

## 用途

通用流程图生成 Skill，可将业务、技术、项目、服务或管理流程转换为可编辑、可导出的标准泳道流程图。

## 主要能力

- 支持 `.drawio`、`.png`、`.vsdx` 和 `.svg` 输出。
- 支持团队、角色、系统和外部参与方作为泳道。
- 默认生成结构校验后的 `.drawio` 与 `.vsdx` 文件。
- 支持 `governance` 主题和自定义主题。

## 使用方式

解压后进入 Skill 目录运行示例：

```bash
cd process-diagram-generator
python3 example_usage.py
```

详细接口、渲染器和主题配置请参考包内的 `SKILL.md` 与 `references/architecture.md`。

## 注意事项

- 导出 PNG 或 VSDX 需要本机安装 draw.io Desktop。
- 可通过 `DRAWIO_PATH` 指定 draw.io Desktop 可执行文件路径。
- `.drawio` 文件可以使用 https://app.diagrams.net/ 打开和继续编辑。

## 文件校验

- 文件：`skills/diagram/process-diagram-generator.zip`
- SHA-256：`c0717cb0e4d10533837e358a87024ec209d0896449113d73e269af3a38d39679`
