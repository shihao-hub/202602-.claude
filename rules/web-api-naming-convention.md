# Web 接口命名规范

本文档定义了 Web API 接口的设计和命名规范，以确保接口的一致性、可读性和可维护性。

## 核心原则

### 1. 路径参数规则

**规则：每个接口最多包含一个路径参数，且必须位于路由的末尾。**

#### 示例

**✅ 推荐写法：**
```
GET    /api/users/{id}              # 获取单个用户
PUT    /api/users/{id}              # 更新用户
DELETE /api/users/{id}              # 删除用户
GET    /api/posts/{postId}/comments # 获取文章的评论列表
```

**❌ 不推荐写法：**
```
GET    /api/users/{userId}/posts/{postId}  # 多个路径参数
GET    /api/{resource}/api/{action}        # 路径参数不在末尾
```

#### 原因说明

- 多个路径参数会增加接口的复杂度和理解成本
- 路径参数位于末尾可以保持路由结构的清晰和层次性
- 如果需要多个参数，应考虑使用查询参数（Query Parameters）

**替代方案：**
```
# 使用查询参数替代多个路径参数
GET /api/users?userId=123&postId=456

# 或拆分为多个接口
GET /api/users/{userId}
GET /api/users/{userId}/posts/{postId}
```

---

### 2. RESTful 风格

**规则：推荐使用 RESTful 风格，但不强制要求。**

#### RESTful 设计建议

| HTTP 方法 | 操作 | 示例 |
|-----------|------|------|
| GET | 查询资源 | `GET /api/users` |
| POST | 创建资源 | `POST /api/users` |
| PUT | 全量更新资源 | `PUT /api/users/{id}` |
| PATCH | 部分更新资源 | `PATCH /api/users/{id}` |
| DELETE | 删除资源 | `DELETE /api/users/{id}` |

#### 非RESTful 风格的容忍

在某些场景下，可以使用非 RESTful 风格的接口命名：

```
POST /api/users/login          # 登录操作
POST /api/users/logout         # 登出操作
POST /api/users/{id}/activate  # 激活用户
POST /api/users/{id}/deactivate # 停用用户
```

**关键原则：** 优先使用 RESTful 风格，但在某些业务场景下可以灵活处理。

---

### 3. 语义化要求

**规则：路由路径 + HTTP 方法应能直接表达接口的业务含义。**

#### 语义化设计指南

**1. 使用名词而非动词**

```
✅ 推荐：
GET /api/users        # 获取用户列表
GET /api/users/{id}   # 获取单个用户
POST /api/users       # 创建用户

❌ 不推荐：
GET /api/getUsers
POST /api/createUser
GET /api/userById
```

**2. 使用复数形式表示资源集合**

```
✅ 推荐：
GET /api/users
GET /api/posts
GET /api/comments

❌ 不推荐：
GET /api/user
GET /api/post
```

**3. 层级结构表达资源关系**

```
✅ 推荐：
GET /api/users/{userId}/posts          # 获取用户的文章
GET /api/posts/{postId}/comments       # 获取文章的评论
POST /api/users/{userId}/posts         # 为用户创建文章

❌ 不推荐：
GET /api/posts?userId={userId}         # 虽然可行，但层级关系不明确
GET /api/user-posts                    # 语义不清晰
```

**4. 使用查询参数进行过滤、排序和分页**

```
✅ 推荐：
GET /api/users?page=1&size=10
GET /api/users?status=active
GET /api/users?sort=name&order=asc
GET /api/posts?category=tech&authorId=123
```

---

## 完整示例

### 用户管理接口

```http
# 用户集合
GET    /api/users              # 获取用户列表
POST   /api/users              # 创建用户

# 单个用户
GET    /api/users/{id}         # 获取用户详情
PUT    /api/users/{id}         # 更新用户信息
DELETE /api/users/{id}         # 删除用户

# 用户相关操作
POST   /api/users/{id}/activate   # 激活用户
POST   /api/users/{id}/deactivate # 停用用户
GET    /api/users/{id}/posts      # 获取用户的文章
```

### 文章管理接口

```http
# 文章集合
GET    /api/posts              # 获取文章列表
POST   /api/posts              # 创建文章

# 单个文章
GET    /api/posts/{id}         # 获取文章详情
PUT    /api/posts/{id}         # 更新文章
DELETE /api/posts/{id}         # 删除文章

# 文章评论
GET    /api/posts/{id}/comments    # 获取文章的评论
POST   /api/posts/{id}/comments   # 为文章添加评论
```

---

## 特殊场景处理

### 1. 搜索接口

```
GET /api/users/search?q=john      # 简单搜索
POST /api/users/search            # 复杂搜索（使用请求体传递搜索条件）
```

### 2. 批量操作

```
POST /api/users/batch-delete      # 批量删除
POST /api/users/batch-update      # 批量更新
```

### 3. 统计接口

```
GET /api/users/stats              # 用户统计
GET /api/posts/{id}/views         # 文章浏览量
```

### 4. 导入导出

```
GET /api/users/export             # 导出用户数据
POST /api/users/import            # 导入用户数据
```

---

## 命名反模式（避免使用）

| 反模式 | 问题 | 改进建议 |
|--------|------|----------|
| `/api/getUserById` | 使用动词，冗余 | 改为 `GET /api/users/{id}` |
| `/api/user` | 使用单数 | 改为 `GET /api/users` |
| `/api/users/{id}/posts/{postId}/comments/{commentId}` | 多层路径参数 | 拆分接口或简化结构 |
| `/api/doSomething` | 语义不明确 | 使用具体的业务术语 |
| `/api/v1/users` 和 `/api/v2/users` 同时存在 | 版本混乱 | 统一版本管理策略 |

---

## 检查清单

在设计新接口时，请确保：

- [ ] 路径参数不超过一个，且位于路由末尾
- [ ] 优先使用 RESTful 风格的 HTTP 方法
- [ ] 路由 + HTTP 方法能清晰表达业务含义
- [ ] 使用名词而非动词命名资源
- [ ] 使用复数形式表示资源集合
- [ ] 合理使用查询参数进行过滤和分页
- [ ] 避免过深的路由层级（建议不超过 3 层）

---

## 相关文档

- [用户故事和测试指南规范](./user-stories-test-guide.md)
- [REST API 设计最佳实践](https://restfulapi.net/)
