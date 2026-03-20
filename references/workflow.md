# PPT Master Workflow Notes

这份参考只保留 Codex 实际执行时最常用的部分。需要更多细节时，再读取上游 `README.md` 或 `docs/quick_reference.md`。

## 能力概览

- 输入源：`PDF`、`URL`、`Markdown`
- 中间产物：项目目录、Markdown 源材料、`设计规范与内容大纲.md`、`svg_output/*.svg`、`notes/total.md`
- 输出：`svg_final/*.svg` 与可编辑 `PPTX`

## 推荐执行顺序

1. 准备运行环境

```bash
.gemini/skills/ppt-master-skill/scripts/bootstrap.sh
```

Python 规则：

- 本 Skill 下的 Python 执行统一使用 `.gemini/skills/ppt-master-skill/.venv`
- 不使用系统 Python，也不把依赖安装到全局环境
- 最稳妥的调用方式是始终走 `scripts/run-python-tool.sh`

2. 转换源材料

```bash
# PDF -> Markdown
.gemini/skills/ppt-master-skill/scripts/run-python-tool.sh pdf_to_md.py ./report.pdf

# 普通网页 -> Markdown
.gemini/skills/ppt-master-skill/scripts/run-python-tool.sh web_to_md.py https://example.com/article

# 微信公众号 / 高防网页 -> Markdown
.gemini/skills/ppt-master-skill/scripts/run-node-tool.sh web_to_md.cjs https://mp.weixin.qq.com/s/xxxx
```

3. 初始化项目并导入材料

```bash
.gemini/skills/ppt-master-skill/scripts/run-python-tool.sh project_manager.py init market_review --format ppt169
.gemini/skills/ppt-master-skill/scripts/run-python-tool.sh project_manager.py import-sources projects/market_review_ppt169_20260320 ./report.pdf ./notes.md
```

4. 在项目目录中完成内容生产

- 先产出或更新 `设计规范与内容大纲.md`
- 再逐页写入 `svg_output/*.svg`
- 最后补齐 `notes/total.md`

5. 后处理与导出

```bash
.gemini/skills/ppt-master-skill/scripts/run-python-tool.sh total_md_split.py projects/market_review_ppt169_20260320
.gemini/skills/ppt-master-skill/scripts/run-python-tool.sh finalize_svg.py projects/market_review_ppt169_20260320
.gemini/skills/ppt-master-skill/scripts/run-python-tool.sh svg_to_pptx.py projects/market_review_ppt169_20260320 -s final
```

## 工具选择建议

| 场景 | 优先工具 | 说明 |
| --- | --- | --- |
| 原生 PDF | `pdf_to_md.py` | 本地、快速、免费 |
| 微信公众号或 403 网页 | `web_to_md.cjs` | Node 版本更稳 |
| 普通网页 | `web_to_md.py` | 足够应对大多数文章页 |
| 项目初始化/归档/校验 | `project_manager.py` | 项目入口 |
| 批量后处理 SVG | `finalize_svg.py` | 自动串联多个 SVG 修复步骤 |
| 导出可编辑 PPTX | `svg_to_pptx.py -s final` | 推荐使用 `svg_final/` |

## 关键项目文件

```text
projects/<name>_<format>_<date>/
├── sources/
├── images/
├── notes/
│   └── total.md
├── svg_output/
├── svg_final/
└── 设计规范与内容大纲.md
```

## 执行提示

- `ppt169` 是最常见的 PowerPoint 16:9 画布格式。
- 设计规范阶段至少确认：画布、页数、受众、风格、配色、图标、图片、排版。
- 导出后的 PPTX 默认以 SVG 嵌入；如需继续细改，在 PowerPoint 中执行“转换为形状”。
