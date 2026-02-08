---
name: web-api-conventions
description: Web API 接口设计和命名规范。在设计、审查或讨论 API 接口时自动应用这些规范，包括路径参数规则、RESTful 风格和语义化要求。
---

# Web 接口命名规范

本 skill 定义了 Web API 接口的设计和命名规范，确保接口的一致性、可读性和可维护性。

## 核心原则

### 1. 路径参数规则

**规则：每个接口最多包含一个路径参数，且必须位于路由的最后一段。**

**✅ 推荐写法：**
```
GET    /api/users/{id}         # 获取单个用户
PUT    /api/users/{id}         # 更新用户
DELETE /api/users/{id}         # 删除用户
GET    /api/comments/{id}      # 获取单条评论
```

**❌ 不推荐写法：**
```
GET    /api/posts/{postId}/comments        # 路径参数不在末尾
GET    /api/users/{userId}/posts/{postId}  # 多个路径参数
GET    /api/{resource}/api/{action}        # 路径参数位置混乱
```

**替代方案（使用查询参数）：**
```
# 需要获取某篇文章的评论时，使用查询参数
GET /api/comments?postId=123

# 需要获取某个用户的文章时，使用查询参数
GET /api/posts?authorId=456

# 需要多个过滤条件时，组合使用查询参数
GET /api/comments?postId=123&status=approved
```

### 2. RESTful 风格

**规则：推荐使用 RESTful 风格，但不强制要求。**

| HTTP 方法 | 操作 | 示例 |
|-----------|------|------|
| GET | 查询资源 | `GET /api/users` |
| POST | 创建资源 | `POST /api/users` |
| PUT | 全量更新资源 | `PUT /api/users/{id}` |
| PATCH | 部分更新资源 | `PATCH /api/users/{id}` |
| DELETE | 删除资源 | `DELETE /api/users/{id}` |

**允许的非 RESTful 风格：**
```
POST /api/users/login          # 登录操作
POST /api/users/logout         # 登出操作
POST /api/users/{id}/activate  # 激活用户
POST /api/users/{id}/deactivate # 停用用户
```

### 3. 语义化要求

**规则：路由路径 + HTTP 方法应能直接表达接口的业务含义。**

**1. 使用名词而非动词**
```
✅ 推荐：
GET /api/users        # 获取用户列表
POST /api/users       # 创建用户

❌ 不推荐：
GET /api/getUsers
POST /api/createUser
```

**2. 使用复数形式表示资源集合**
```
✅ 推荐：GET /api/users
❌ 不推荐：GET /api/user
```

**3. 使用查询参数表达资源关联关系**
```
✅ 推荐：
GET /api/posts?authorId=123            # 获取指定用户的文章
GET /api/comments?postId=456           # 获取指定文章的评论

❌ 不推荐：
GET /api/users/{userId}/posts          # 路径参数不在末尾
GET /api/posts/{postId}/comments       # 路径参数不在末尾
```

## 特殊场景处理

**搜索接口：**
```
GET /api/users/search?q=john      # 简单搜索
POST /api/users/search            # 复杂搜索
```

**批量操作：**
```
POST /api/users/batch-delete      # 批量删除
POST /api/users/batch-update      # 批量更新
```

**统计接口：**
```
GET /api/users/stats              # 用户统计
GET /api/post-views/{id}          # 文章浏览量
```

**导入导出：**
```
GET /api/users/export             # 导出用户数据
POST /api/users/import            # 导入用户数据
```

## 检查清单

在设计新接口时，确保：

- [ ] 路径参数不超过一个，且必须位于路由的最后一段
- [ ] 优先使用 RESTful 风格的 HTTP 方法
- [ ] 路由 + HTTP 方法能清晰表达业务含义
- [ ] 使用名词而非动词命名资源
- [ ] 使用复数形式表示资源集合
- [ ] 合理使用查询参数进行过滤、分页和表达资源关联
- [ ] 避免过深的路由层级（建议不超过 2 层）
