# Claude Code 全局配置目录

这是 Claude Code 的全局配置目录，包含自定义指令、技能、插件、钩子等配置文件。

## 目录结构

```
.claude/
├── .gitignore          # Git 忽略规则（白名单模式）
├── claude.md           # 全局指令配置
├── settings.json       # Claude Code 设置
├── commands/           # 自定义命令
├── skills/             # 自定义技能
├── hooks/              # 钩子脚本
├── agents/             # AI 代理配置
├── plugins/            # 插件目录
├── docs/               # 项目文档
├── projects/           # 项目相关文件
└── tasks/              # 任务管理文件
```

## 主要配置文件

### claude.md
全局指令文件，定义了 Claude 在所有项目中应遵循的行为规范：
- Git 提交规范
- README.md 自动更新
- .gitignore 智能维护
- 关键回答持久化
- 文档命名规范

### settings.json
Claude Code 的核心配置文件，包含编辑器、模型、UI 等设置。

### .gitignore
采用白名单模式，默认忽略所有文件，仅显式允许特定文件和目录被跟踪。

## 使用说明

### 全局指令
所有项目都会自动应用 `claude.md` 中定义的指令，包括：
- 每次修改后自动提交到 git
- 自动更新 README.md
- 智能维护 .gitignore
- 将关键回答持久化为文档

### 自定义技能
在 `skills/` 目录中可以添加自定义技能，扩展 Claude 的能力。

### 自定义命令
在 `commands/` 目录中可以添加自定义命令，简化常用操作。

### AI 代理
在 `agents/` 目录中可以配置专门的 AI 代理处理特定任务。

### 项目文档
在 `docs/` 目录中包含详细的使用文档：
- [Claude Code Hooks 示例](docs/claude-code-hooks-example.md) - hooks 配置和使用指南

## Commit 规范

本项目遵循以下 commit message 规范：

```
<type>(<scope>): <subject>（中文，≤50字，动词开头，无句号）

可选正文（说明"是什么"和"为什么"，每行≤72字符，用 - 列表）

可选页脚（如 BREAKING CHANGE: 或 Closes #xxx）
```

**Type 类型：**
- `feat`：新功能
- `fix`：修复 bug
- `docs`：文档变更
- `style`：代码格式（不影响功能）
- `refactor`：重构
- `perf`：性能优化
- `test`：测试
- `chore`：构建/工具变更
- `ci`：CI 配置
- `revert`：回退

**动词参考：**
添加、修复、优化、重构、移除、更新、升级、集成

## 维护说明

### 更新配置
1. 修改相应的配置文件
2. Claude 会自动提交更改
3. 如需手动提交，遵循上述 commit 规范

### 添加新技能
1. 在 `skills/` 目录创建技能文件
2. 按照 Claude Code 技能规范编写
3. 确保 .gitignore 包含该文件类型

### 版本控制
- 当前分支：`master`
- 远程仓库：`origin/main`
- 使用白名单模式的 .gitignore，确保所有新增文件都被显式允许

## 许可证

本配置为个人 Claude Code 使用环境，包含自定义配置和指令。

## 更新日志

### 2026-02-05
- 添加 docs 目录到 .gitignore 白名单
- 新增 Claude Code Hooks 示例文档

### 2026-02-04
- 添加 agents 目录到 .gitignore 白名单
- 创建项目 README.md 文档
- 完善项目结构说明
