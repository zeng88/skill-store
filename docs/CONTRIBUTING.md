# 贡献与发布规范

## 添加 Skill

1. 每个 Skill 使用一个独立 `.zip` 文件，不要把未打包的运行目录混入 `skills/`。
2. 按业务归档到 `skills/<分类>/`，目录名使用小写字母、数字和下划线。
3. 文件名建议为 `{功能名称}_{版本}.zip`，单文件建议小于 100 MB。
4. 在 `docs/<分类>/` 增加同名说明文档，至少包含用途、依赖、配置参数、调用示例和 SHA-256。
5. 运行下载清单脚本并检查 Git diff：

```bash
python3 scripts/gen_download_links.py
python3 -m unittest discover -s tests -v
```

## 安全检查

- 压缩包内不得包含 API Key、密码、Cookie、私钥或个人隐私数据。
- 提交前检查压缩包内容：`unzip -l path/to/skill.zip`。
- 对外发布前记录 SHA-256，方便下载方校验文件完整性。

## Release 建议

需要长期稳定地址或版本回滚时，把 Skill zip 作为 GitHub Release 附件发布，并在文档中保留对应版本的校验值。
