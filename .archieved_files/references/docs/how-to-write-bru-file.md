# BRU 文件编写指南

## 什么是 .bru 文件？

`.bru` 是 Bruno API 客户端使用的**纯文本请求定义文件格式**，基于一种称为 **Bru Markup Language (Bru Lang)** 的 DSL（领域特定语言）。

### 核心特性

- **纯文本格式**：易于阅读、编写和版本控制
- **声明式语法**：通过标签块描述请求结构
- **Git 友好**：适合团队协作和代码审查
- **支持脚本**：可使用 JavaScript 扩展功能

---

## 基本语法结构

### 标签块语法

`.bru` 文件由一系列**标签（Tags）**组成，每个标签后跟一个用大括号 `{}` 包裹的**值块**。

```bru
<标签> {
  <值>
}
```

**语法规则**：
- 标签名**不区分大小写**（通常使用小写）
- 值块可以是单行或多行
- 空白行会被忽略
- 无需行尾逗号

---

## 核心标签参考

### 1. 元数据块 (meta)

定义请求的基础信息。

```bru
meta {
  name: 获取用户列表        # 请求名称
  type: http                # 请求类型：http / graphql
  seq: 1                    # UI 中的排序序号
  tags: [smoke, sanity]     # 标签分类
}
```

### 2. HTTP 方法块

定义请求方法和主要配置，**必须且只能有一个**。

| 标签 | 说明 |
|------|------|
| `get` | GET 请求 |
| `post` | POST 请求 |
| `put` | PUT 请求 |
| `patch` | PATCH 请求 |
| `delete` | DELETE 请求 |
| `head` | HEAD 请求 |
| `options` | OPTIONS 请求 |

```bru
post {
  url: {{baseUrl}}/api/users    # 请求 URL
  body: json                    # 请求体类型
  auth: bearer                  # 认证类型
}
```

### 3. URL 参数块 (query)

定义 URL 查询参数。

```bru
query {
  page: 1
  limit: 20
  search: {{keyword}}
}
```

### 4. 请求头块 (headers)

定义 HTTP 请求头。

```bru
headers {
  Content-Type: application/json
  Authorization: Bearer {{authToken}}
  X-Custom-Header: custom-value
}
```

### 5. 请求体块 (body)

支持多种数据格式。

| 格式 | 说明 |
|------|------|
| `body:json` | JSON 格式 |
| `body:text` | 纯文本 |
| `body:xml` | XML 格式 |
| `body:form-urlencoded` | 表单编码 |
| `body:multipart-form` | 多部分表单 |

```bru
body:json {
  {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
  }
}
```

### 6. 认证块 (auth)

配置请求认证方式，支持覆盖集合或工作区的认证设置。

```bru
auth:bearer {
  token: {{accessToken}}
}

# 或使用继承
auth:inherit
```

### 7. 文档块 (docs)

为请求添加 Markdown 格式的说明文档。

```bru
docs {
  ## 接口说明
  创建新用户账户

  **权限要求**：需要管理员权限

  **返回示例**：
  ```json
  {"id": 123, "status": "created"}
  ```
}
```

---

## 变量系统

### 变量插值语法

使用 `{{variableName}}` 在任何地方进行变量插值。

```bru
url: {{baseUrl}}/api/{{version}}/users
headers {
  Authorization: Bearer {{authToken}}
}
```

### 变量来源优先级

1. **全局变量** (Global Variables)
2. **环境变量** (Environment Variables)
3. **集合变量** (Collection Variables)
4. **文件夹变量** (Folder Variables)
5. **请求变量** (Request Variables)

### 变量提取 (vars:post-response)

从响应中提取变量供后续请求使用（Request Chaining）。

```bru
vars:post-response {
  token: res.body.access_token
  userId: res.body.data.id
  orderId: res.body.order.id
}
```

---

## 脚本编写

### 脚本类型

| 脚本类型 | 说明 |
|----------|------|
| `script:pre-request` | 请求前执行 |
| `script:post-response` | 响应后执行 |
| `tests` | 测试脚本 |

### 内置对象

| 对象 | 说明 |
|------|------|
| `req` | 请求对象，可读取或修改请求 |
| `res` | 响应对象，获取响应结果 |
| `bru` | Bruno 核心对象，操作变量链 |

### 常用 API

```javascript
// bru 对象方法
bru.setVar("key", "value")        // 设置变量
bru.getVar("key")                 // 获取变量
bru.getEnvVar("key")              // 获取环境变量

// req 对象方法
req.setBody(data)                 // 设置请求体
req.setHeader("Name", "Value")    // 设置请求头

// res 对象方法
res.getStatus()                   // 获取状态码
res.getBody()                     // 获取响应体
```

### 引入外部库

```bru
script:pre-request {
  // 使用 Node.js 内置库
  const uuid = require('uuid');
  bru.setVar("reqId", uuid.v4());

  // 引入自定义脚本
  const utils = require('./utils.js');
  const timestamp = utils.getTimestamp();
  bru.setVar("timestamp", timestamp);
}
```

---

## 断言与测试

### 声明式断言 (assert)

无需编写 JavaScript 即可完成测试。

```bru
assert {
  res.status: eq 200                    # 状态码等于 200
  res.body.status: equals success       # 字段等于指定值
  res.body.message: contains created    # 包含特定文本
  res.body.users: isNotEmpty            # 非空检查
  res.body.users[0].name: eq Alice      # 嵌套/数组断言
}
```

**常用运算符**：
- `eq` / `equals`: 等于
- `contains`: 包含
- `isNotEmpty`: 非空
- `gt` / `lt`: 大于 / 小于

### JavaScript 测试

```bru
tests {
  // 状态码断言
  bru.assert(res.getStatus() === 200);

  // 响应体断言
  const body = res.getBody();
  bru.assert(body.id === 1);
  bru.assert(body.title.includes("test"));

  // 性能断言
  const responseTime = res.getResponseTime();
  bru.assert(responseTime < 1000);
}
```

---

## 完整示例

### 示例 1：简单 GET 请求

```bru
meta {
  name: 获取用户信息
  type: http
}

get {
  url: https://api.example.com/users/{{userId}}
}

headers {
  Authorization: Bearer {{apiKey}}
}
```

### 示例 2：POST 请求与测试

```bru
meta {
  name: 创建新订单
  type: http
  seq: 1
}

post {
  url: {{baseUrl}}/api/orders
  body: json
  auth: bearer
}

headers {
  Content-Type: application/json
  X-Request-ID: {{reqId}}
}

auth:bearer {
  token: {{accessToken}}
}

body:json {
  {
    "itemId": 99,
    "quantity": 1,
    "notes": "请尽快发货"
  }
}

script:pre-request {
  const uuid = require('uuid');
  bru.setVar("reqId", uuid.v4());
}

vars:post-response {
  orderId: res.body.data.orderId
}

assert {
  res.status: eq 201
  res.body.success: eq true
  res.body.data.orderId: isNotEmpty
}
```

### 示例 3：带文档的复杂请求

```bru
meta {
  name: 批量导入用户
  type: http
  tags: [batch, admin]
}

post {
  url: {{baseUrl}}/api/users/batch
  body: json
}

docs {
  ## 批量导入用户接口

  用于批量创建用户账户，单次最多支持 100 条记录。

  **权限**：需要管理员角色

  **限制**：
  - 单次最多 100 条
  - 每小时最多 1000 次

  **错误码**：
  - 400: 参数错误
  - 401: 未授权
  - 429: 请求过于频繁
}

body:json {
  {
    "users": [
      {"name": "Alice", "email": "alice@example.com"},
      {"name": "Bob", "email": "bob@example.com"}
    ]
  }
}

tests {
  bru.assert(res.getStatus() === 201);
  const body = res.getBody();
  bru.assert(body.success === true);
  bru.assert(body.createdCount === 2);
}
```

---

## 最佳实践

### 1. 模块化组织

将相关请求组织到文件夹中，共享文件夹级别的变量和认证。

```
collection/
├── bru-config.json
├── environments/
│   ├── development.bru
│   └── production.bru
└── users/
    ├── folder.bru          # 文件夹级别的认证和变量
    ├── list-users.bru
    ├── get-user.bru
    └── create-user.bru
```

### 2. 使用变量避免硬编码

```bru
# 好的做法
url: {{baseUrl}}/api/{{version}}/users
Authorization: Bearer {{apiKey}}

# 避免
url: https://api.example.com/v1/users
Authorization: Bearer sk_live_1234567890
```

### 3. 编写测试覆盖

为关键 API 添加 `assert` 或 `tests` 块。

```bru
assert {
  res.status: eq 200
  res.body.success: eq true
  res.body.data: isNotEmpty
}
```

### 4. 添加文档说明

使用 `docs` 块为复杂请求提供上下文。

```bru
docs {
  ## 支付回调接口

  处理第三方支付平台的异步回调通知。

  **签名验证**：使用 HMAC-SHA256
  **幂等性**：支持重复通知
}
```

### 5. 版本控制友好

- `.bru` 文件是纯文本，适合 Git 管理
- 使用 `.gitignore` 排除敏感信息（如包含真实密钥的环境文件）
- 为每个请求添加有意义的 `name` 便于代码审查

---

## 附录：快速参考

### 完整文件结构

```bru
meta { }
get { } | post { } | put { } | delete { }
query { }
headers { }
auth:type { }
body:type { }
script:pre-request { }
vars:post-response { }
assert { }
tests { }
docs { }
```

### 常用认证类型

| 类型 | 配置块 |
|------|--------|
| Bearer | `auth:bearer { token: xxx }` |
| Basic | `auth:basic { username: xxx, password: xxx }` |
| API Key | `auth:api-key { key: xxx, value: xxx }` |
| Inherit | `auth:inherit` |

---

> **文档版本**：1.0.0
> **最后更新**：2026-02-22
> **参考来源**：[Bruno 官方文档](https://docs.usebruno.com)
