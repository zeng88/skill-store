# Flowchart Generator

## 用途

面向审计和财务场景的 AI 流程图 Skill，可将自然语言流程转换为标准泳道流程图，并支持样式主题管理。

## 主要能力

- 生成 `.drawio`、`.png`、`.vsdx` 和 `.svg` 等格式。
- 使用 `governance` 内控搭建主题，输出适合内控手册的专业样式。
- 通过核心引擎校验节点、连线和流程结构。

## 使用方式

解压后进入 Skill 目录运行示例：

```bash
cd flowchart-generator
python3 example_usage.py
```

也可以在 Python 中导入 `engine.StyleManager` 和 `engine.FlowchartBuilder`，按包内 README 与 `SKILL.md` 组装流程节点。

## 注意事项

- 导出 PNG 或 VSDX 需要本机安装 draw.io Desktop。
- `.drawio` 文件可以使用 https://app.diagrams.net/ 打开和继续编辑。

## 文件校验

- 文件：`skills/diagram/flowchart-generator.zip`
- SHA-256：`03ecc6c3df097b8fcd38df1cd365e667506c0909b46ec079d91ef62a078b1bc9`
