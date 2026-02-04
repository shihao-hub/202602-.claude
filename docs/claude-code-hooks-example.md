# Claude Code Hooks 示例

本文档提供了 Claude Code hooks 的实用配置示例，用于在特定事件触发时自动执行自定义命令。

## 什么是 Hooks？

Hooks 允许您在 Claude Code 的各种事件发生时执行自定义的 shell 命令，例如：
- 在工具调用前/后
- 在用户提交输入前
- 在响应显示前

## 配置位置

Hooks 配置在 `settings.json` 文件的 `hooks` 字段中：

```json
{
  "hooks": {
    "<hook-name>": "<command-to-execute>"
  }
}
```

## 常用 Hook 类型

### 1. 工具调用前 Hook

在调用指定工具前执行命令：

```json
{
  "hooks": {
    "tool-call-pre-Bash(*)": "echo '准备执行 Bash 命令'",
    "tool-call-pre-Edit(*)": "echo '准备编辑文件'",
    "tool-call-pre-Write(*)": "echo '准备写入文件'"
  }
}
```

### 2. 工具调用后 Hook

在调用指定工具后执行命令：

```json
{
  "hooks": {
    "tool-call-post-Bash(*)": "echo 'Bash 命令执行完毕'",
    "tool-call-post-Edit(*)": "echo '文件编辑完成'",
    "tool-call-post-Write(*)": "echo '文件写入完成'"
  }
}
```

### 3. 用户输入提交 Hook

在用户提交输入前执行命令：

```json
{
  "hooks": {
    "user-prompt-submit-hook": "echo '用户提交了新输入'"
  }
}
```

### 4. 响应显示前 Hook

在响应显示给用户前执行：

```json
{
  "hooks": {
    "pre-response-hook": "echo '准备显示响应'"
  }
}
```

## 实用示例

### 示例 1：自动记录操作日志

```json
{
  "hooks": {
    "tool-call-post-Edit(*)": "powershell -Command \"Add-Content -Path 'C:\\Users\\29580\\.claude\\logs\\edits.log' -Value ('$(Get-Date -Format \"yyyy-MM-dd HH:mm:ss\"): Edited $CLAUDE_FILE_PATH')\""
  }
}
```

### 示例 2：代码格式化检查

```json
{
  "hooks": {
    "tool-call-pre-Write(*.ts,*.tsx,*.js,*.jsx)": "npm run format-check || echo '提示: 建议先格式化代码'"
  }
}
```

### 示例 3：Git 状态提醒

```json
{
  "hooks": {
    "tool-call-post-Edit(*),tool-call-post-Write(*)": "git status --short || true"
  }
}
```

### 示例 4：自动备份重要文件

```json
{
  "hooks": {
    "tool-call-pre-Edit(settings.json,CLAUDE.md)": "powershell -Command \"Copy-Item '$CLAUDE_FILE_PATH' -Destination ('$CLAUDE_FILE_PATH.bak') -Force\""
  }
}
```

### 示例 5：环境变量验证

```json
{
  "hooks": {
    "tool-call-pre-Bash(git *)": "powershell -Command \"if (-not (git rev-parse --git-dir 2>$null)) { Write-Host '警告: 当前目录不是 Git 仓库' }\""
  }
}
```

## 环境变量

在 hooks 中可以使用以下环境变量：

- `$CLAUDE_FILE_PATH` - 当前操作的文件路径
- `$CLAUDE_TOOL_NAME` - 当前调用的工具名称
- `$CLAUDE_WORKING_DIR` - 当前工作目录

## 通配符支持

工具名称支持通配符匹配：

- `*` - 匹配任意字符
- `Bash(*)` - 匹配所有 Bash 工具调用
- `Edit(*.md)` - 匹配所有 .md 文件的编辑

## 注意事项

1. **性能影响**: Hooks 会增加额外执行时间，避免在 hooks 中执行耗时操作
2. **错误处理**: 建议在命令末尾添加 `|| true` 防止命令失败阻断主流程
3. **权限配置**: 确保 hooks 中使用的命令已在 `permissions.allow` 中授权
4. **Windows 兼容**: 在 Windows 系统中，建议使用 `powershell` 或 `pwsh` 命令

## 完整配置示例

```json
{
  "hooks": {
    "tool-call-post-Edit(*),tool-call-post-Write(*)": "git status --short || true",
    "tool-call-pre-Write(settings.json)": "powershell -Command \"if (Test-Path 'settings.json') { Copy-Item 'settings.json' 'settings.json.bak' -Force }\"",
    "user-prompt-submit-hook": "powershell -Command \"Add-Content -Path 'C:\\Users\\29580\\.claude\\logs\\activity.log' -Value ('$(Get-Date -Format \"yyyy-MM-dd HH:mm:ss\"): User prompt submitted')\""
  }
}
```

## 调试技巧

如需调试 hooks，可以在命令中添加日志输出：

```json
{
  "hooks": {
    "tool-call-pre-Edit(*)": "powershell -Command \"Write-Host '[DEBUG] Hook triggered for: $env:CLAUDE_FILE_PATH'\""
  }
}
```

## 相关资源

- [Claude Code 官方文档](https://docs.anthropic.com/claude-code)
- [Settings.json 配置参考](https://docs.anthropic.com/claude-code/settings)
