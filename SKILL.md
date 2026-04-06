---
name: ppt-master-skill
description: 基于 macrochen/ppt-master 工作流，将 PDF、URL 或 Markdown 材料转成可编辑 PowerPoint 项目与 PPTX。适用于初始化项目、导入源材料、运行 SVG 后处理与导出、以及按 Strategist/Executor 流程生成演示文稿。
---

# PPT Master Skill

使用这个 Skill 来调用 `ppt-master`，适合这些场景：

- 用户明确提到 `ppt-master`、`PPT Master` 或仓库 `macrochen/ppt-master`
- 想把 PDF、网页或 Markdown 材料整理成可编辑 PPT
- 想生成 `svg_output/`、`svg_final/` 和最终 `.pptx`
- 想复用 `ppt-master` 的项目结构、工具链和 Strategist / Executor 工作流

## Runtime

首次使用先执行：

```bash
~/.agents/skills/ppt-master-skill/scripts/bootstrap.sh
```

之后优先通过包装脚本运行上游工具：

```bash
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh project_manager.py init demo --format ppt169
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh project_manager.py import-sources projects/demo_ppt169_20260320 ./source.pdf
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh finalize_svg.py projects/demo_ppt169_20260320
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh svg_to_pptx.py projects/demo_ppt169_20260320 -s final
```

网页转 Markdown 时：

```bash
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh web_to_md.py https://example.com/article
~/.agents/skills/ppt-master-skill/scripts/run-node-tool.sh web_to_md.cjs https://mp.weixin.qq.com/s/xxxx
```

Python 相关约束：

- 本 Skill 的所有 Python 脚本必须且只能在当前 Skill 目录下的 `.venv` 中执行。
- 不要使用系统 Python、全局 `pip`、或其他目录下的虚拟环境替代。
- 如环境缺失，先运行 `scripts/bootstrap.sh` 创建并安装 `.venv`，再继续执行。

## Working Rules

- 默认优先复用上游 `vendor/ppt-master` 里的工具，不重写同类流程。
- 第一次使用、缺少 `vendor/ppt-master`、或依赖失效时，先运行 `bootstrap.sh`。
- 任何 Python 工具调用都必须通过 `~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh` 或该 Skill 自己的 `.venv/bin/python` 执行，不得直接调用系统 Python。
- 需要 PDF 输入时，优先运行 `pdf_to_md.py`；结果明显错乱、扫描件或 OCR 失败时再说明需要人工兜底。
- 需要 URL 输入时，普通网页优先 `web_to_md.py`；微信公众号或出现 403 时改用 `web_to_md.cjs`。
- 正式生成前，先用 `project_manager.py init` 创建项目，再用 `import-sources` 把源材料归档到项目目录。
- 若用户只给主题没有现成材料，也可以直接初始化项目并在项目内产出 `设计规范与内容大纲.md`、`svg_output/` 和 `notes/total.md`。
- 设计阶段沿用上游约定：先完成画布格式、页数、受众、风格、配色、图标、图片、排版等确认，再开始出图。
- 页面产出完成后，默认顺序是 `total_md_split.py` -> `finalize_svg.py` -> `svg_to_pptx.py -s final`。
- 用户关心“是否可编辑”时，要说明导出的 PPTX 以 SVG 形式嵌入；在 Office 2016+ 中可通过 “转换为形状” 继续编辑。
- 如果需要更完整的命令矩阵、角色分工或项目结构，再读取 `references/workflow.md`。

## Default Flow

1. 判断输入源类型：`PDF`、`URL`、`Markdown` 或纯主题。
2. 如需，先将源内容转换为 Markdown。
3. 初始化项目并归档源材料。
4. 生成或完善 `设计规范与内容大纲.md`。
5. 按页面生成 `svg_output/*.svg`，并补齐 `notes/total.md`。
6. 运行后处理与导出，得到最终 `.pptx`。

## Useful Commands

```bash
~/.agents/skills/ppt-master-skill/scripts/bootstrap.sh
~/.agents/skills/ppt-master-skill/scripts/bootstrap.sh --update
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh project_manager.py validate projects/<project>
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh pdf_to_md.py ./report.pdf
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh total_md_split.py projects/<project>
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh finalize_svg.py projects/<project>
~/.agents/skills/ppt-master-skill/scripts/run-python-tool.sh svg_to_pptx.py projects/<project> -s final
```

## Read More Only When Needed

- `references/workflow.md`: 常用命令、项目结构、工具选择建议
- `vendor/ppt-master/README.md`: 上游总览与能力边界
- `vendor/ppt-master/docs/quick_reference.md`: 上游角色与执行清单
