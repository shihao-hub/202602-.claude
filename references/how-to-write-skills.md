根据搜索结果，以下是如何编写 Skills 的方法：

## 创建 Skills

在 `.claude/skills/` 目录下创建包含 `SKILL.md` 文件的文件夹。Skills 可以扩展 Claude 的知识，Claude 会在相关时自动应用它们，或者你可以用 `/skill-name` 直接调用。

### 基本结构

```markdown
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
```

### 关键字段

| 字段 | 用途 |
|:--|:--|
| `name` | Skill 名称 |
| `description` | 描述，帮助 Claude 判断何时使用 |
| `disable-model-invocation` | 设为 `true` 时，只有用户手动调用才会触发 |

### 使用参数

使用 `$ARGUMENTS` 占位符接收用户输入：

```markdown
---
description: Greet the user with a personalized message
---
Greet the user named "$ARGUMENTS" warmly.
```

调用时：`/skill-name Alex`

更多详情请参考 [Skills 文档](/en/skills)。

```suggestions
(Extend Claude with skills)[/en/skills]
(Create plugins)[/en/plugins]
(Best Practices for Claude Code)[/en/best-practices]
```