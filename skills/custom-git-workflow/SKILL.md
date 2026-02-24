---
name: custom-git-workflow
description: Git 提交和推送自动化流程。检查变更、生成符合规范的提交消息、提交更改并推送到远程仓库。
---

# Git 提交和推送指南

本 skill 提供了一套完整的 Git 工作流程，用于检查变更、创建符合规范的提交消息并推送到远程仓库。

## 工作流程

### 1. 检查 Git 状态

首先检查当前仓库的变更状态：

```bash
git status
```

这会显示所有已修改、新增和删除的文件。

### 2. 查看变更内容

查看具体的代码变更，以便撰写准确的提交消息：

```bash
# 查看已暂存的变更
git diff --cached

# 查看未暂存的变更
git diff

# 查看最近的提交历史（了解提交风格）
git log --oneline -10
```

### 3. 分析变更并确定提交类型

根据变更内容，确定合适的提交类型（type）和作用范围（scope）：

| Type | 说明 | 示例 |
|:---|:---|:---|
| `feat` | 新功能 | 添加用户认证功能 |
| `fix` | Bug 修复 | 修复登录页面布局错误 |
| `docs` | 文档变更 | 更新 README 安装说明 |
| `style` | 代码格式（不影响功能） | 统一缩进格式 |
| `refactor` | 重构（不是新功能也不是修复）| 重构用户服务模块 |
| `perf` | 性能优化 | 优化数据库查询 |
| `test` | 测试相关 | 添加单元测试 |
| `chore` | 构建/工具/辅助工具变更 | 更新依赖包 |
| `ci` | CI/CD 配置变更 | 添加 GitHub Action |
| `revert` | 回退提交 | 回退 commit abc123 |

### 4. 撰写提交消息

#### 规范格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### 必填部分

**标题行（必填）：**
- 格式：`<type>(<scope>): <subject>`
- `type`：变更类型（见上表）
- `scope`：影响范围（可选），如 `auth`、`db`、`api` 等
- `subject`：简短描述（中文，≤50 字，动词开头，无句号）

**示例：**
```
feat(auth): 添加 JWT 认证功能
fix(api): 修复用户列表接口返回数据错误
docs(readme): 更新安装步骤说明
```

#### 可选部分

**正文（body，可选）：**
- 详细说明"是什么"和"为什么"
- 每行 ≤ 72 字符
- 使用 `-` 列表格式

**页脚（footer，可选）：**
- 破坏性变更：`BREAKING CHANGE: 详细说明`
- 关联 issue：`Closes #123`

#### 完整示例

```
feat(auth): 添加基于 JWT 的用户认证功能

- 实现用户登录接口 `/api/auth/login`
- 实现令牌刷新接口 `/api/auth/refresh`
- 添加认证中间件保护需要登录的接口
- 令牌有效期为 2 小时

Closes #42
```

### 5. 暂存变更

根据需要暂存要提交的文件：

```bash
# 暂存所有变更
git add .

# 暂存特定文件
git add <file1> <file2>

# 交互式暂存
git add -i
```

### 6. 提交变更

使用撰写的提交消息进行提交：

```bash
git commit -m "<type>(<scope>): <subject>"
```

对于多行提交消息，使用 HEREDOC 格式：

```bash
git commit -m "$(cat <<'EOF'
<type>(<scope>): <subject>

<body>

<footer>
EOF
)"
```

### 7. 推送到远程仓库

```bash
# 推送到当前分支的远程追踪分支
git push

# 推送到指定远程和分支
git push <remote> <branch>

# 首次推送并设置上游分支
git push -u origin <branch>
```

## 快捷命令

以下是一些有用的快捷命令：

```bash
# 查看状态和变更摘要
git status && git diff --stat

# 查看最近 5 条提交
git log --oneline -5

# 修改最后一次提交消息
git commit --amend

# 取消暂存
git restore --staged <file>

# 放弃工作区变更
git restore <file>
```

## 注意事项

- **推送前检查**：确认提交消息准确描述了变更内容
- **避免敏感信息**：不要提交密码、密钥等敏感数据
- **提交粒度**：保持每次提交聚焦于单一逻辑变更
- **测试验证**：推送前确保相关测试通过
- **分支保护**：推送到受保护的分支可能需要 PR 流程

## 检查清单

提交前确认：

- [ ] 已查看 `git status` 了解所有变更
- [ ] 提交类型正确（feat/fix/docs 等）
- [ ] 标题简明扼要（≤50 字，动词开头）
- [ ] 没有提交敏感信息
- [ ] 相关测试已通过
- [ ] 提交消息清晰说明了变更目的
