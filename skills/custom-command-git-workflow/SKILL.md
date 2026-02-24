---
name: custom-command-git-workflow
description: Git 提交和推送自动化流程。检查变更、生成符合规范的提交消息、提交更改并推送到远程仓库。
disable-model-invocation: true
---

# Git 提交和推送命令

## 执行指令

当用户调用此命令时，按以下步骤执行：

### 步骤 1：检查 Git 状态

执行 `git status` 查看当前变更，向用户展示变更摘要。

### 步骤 2：查看变更内容

执行以下命令查看具体修改：
- `git diff` - 查看未暂存的变更
- `git diff --cached` - 查看已暂存的变更
- `git log --oneline -5` - 查看最近的提交记录

### 步骤 3：分析变更并生成提交消息

根据变更内容分析：
- 确定提交类型（feat/fix/docs/refactor等）
- 确定影响范围（scope）
- 生成提交标题（≤50字，中文，动词开头）
- 如需要，生成提交正文

### 步骤 4：确认提交消息

向用户展示生成的提交消息，询问是否确认或需要修改。

### 步骤 5：暂存和提交

- 使用 `git add` 暂存文件（通常 `git add .`）
- 使用 `git commit -m "..."` 提交
- 使用 HEREDOC 格式处理多行提交消息

### 步骤 6：推送

执行 `git push` 推送到远程仓库。

### 步骤 7：验证

展示提交结果，确认推送成功。

---

## 提交消息规范

### 类型（type）

| Type | 说明 |
|:---|:---|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `docs` | 文档变更 |
| `style` | 代码格式（不影响功能） |
| `refactor` | 重构 |
| `perf` | 性能优化 |
| `test` | 测试相关 |
| `chore` | 构建/工具/辅助工具变更 |
| `ci` | CI/CD 配置变更 |
| `revert` | 回退提交 |

### 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

- `scope`：影响范围（可选），如 `auth`、`db`、`api`
- `subject`：简短描述（中文，≤50 字，动词开头，无句号）

### 示例

```
feat(auth): 添加基于 JWT 的用户认证功能

- 实现用户登录接口 `/api/auth/login`
- 实现令牌刷新接口 `/api/auth/refresh`
- 添加认证中间件保护需要登录的接口

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

## 注意事项

- 提交前确认没有敏感信息（密码、密钥等）
- 推送前确认相关测试已通过
- 保持每次提交聚焦于单一逻辑变更
