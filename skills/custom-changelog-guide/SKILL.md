---
name: custom-changelog-guide
description: CHANGELOG.md 编写指南和最佳实践。在创建、更新或维护项目变更日志时使用，包括 Keep a Changelog 规范、版本记录结构和自动化工具建议。
---

# CHANGELOG.md 编写指南

本 skill 提供了 CHANGELOG.md 的编写规范和最佳实践，确保项目的版本变更历史清晰、可追溯。

## 什么是 CHANGELOG.md

CHANGELOG.md（通常写作 CHANGELOG.md，单数形式更常见）是一个用于记录项目版本变更历史的文件。它通常以 Markdown 格式编写，放在软件项目的根目录中。

### 主要作用

| 作用 | 说明 |
|:---|:---|
| **透明性** | 清楚展示项目演进过程 |
| **可追溯性** | 便于排查问题或理解某个功能何时引入 |
| **升级参考** | 帮助用户判断是否需要升级，以及升级时需要注意什么 |
| **协作便利** | 为团队成员和外部贡献者提供清晰的变更上下文 |

## Keep a Changelog 规范

推荐遵循 [Keep a Changelog](https://keepachangelog.com/) 规范和 [语义化版本](https://semver.org/lang/zh-CN/)。

### 标准结构模板

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 新功能描述...

### Changed
- 修改的内容...

### Deprecated
- 即将废弃的功能...

### Removed
- 已移除的内容...

### Fixed
- 修复的 bug...

### Security
- 安全相关修复...

## [1.0.0] - 2025-01-15

### Added
- 初始版本发布
```

### 分类说明

| 分类 | 用途 | 示例 |
|:---|:---|:---|
| **Added** | 新增的功能 | `- 添加用户认证功能` |
| **Changed** | 现有功能的变更 | `- 修改登录接口的返回格式` |
| **Deprecated** | 即将移除的功能 | `- 旧版 API 将在 2.0 废弃` |
| **Removed** | 已移除的功能 | `- 移除对 Node.js 14 的支持` |
| **Fixed** | Bug 修复 | `- 修复登录页面在 Safari 下布局错位的问题` |
| **Security** | 安全相关 | `- 修复 SQL 注入漏洞` |

## 编写小贴士

### ✅ 推荐做法

```markdown
### Fixed
- 修复登录页面在 Safari 14 下布局错位的问题
- 修复用户导出功能在超过 1000 条记录时超时的问题

### Added
- 添加用户头像上传功能，支持 JPG、PNG 格式，最大 5MB
```

### ❌ 不推荐做法

```markdown
### Fixed
- 修复 bug
- 修复问题
- 优化代码

### Changed
- 一些改动
```

**关键点：**
- 避免模糊描述，具体说明修复了什么问题
- 说明影响范围（如特定浏览器、特定条件）
- 对于新功能，说明使用限制或要求

## 自动化工具

以下工具可以根据 Git 提交信息自动生成 changelog：

| 工具 | 语言 | 特点 |
|:---|:---|:---|
| [standard-version](https://github.com/conventional-changelog/standard-version) | Node.js | 遵循 Conventional Commits |
| [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog) | Node.js | 可定制化程度高 |
| [towncrier](https://towncrier.readthedocs.io/) | Python | 使用碎片文件构建 |
| [release-drafter](https://github.com/release-drafter/release-drafter) | GitHub Action | 自动生成 GitHub Release |

## 文件命名

常见变体（按推荐顺序）：

- `CHANGELOG.md` （最常见，推荐）
- `CHANGES.md`
- `HISTORY.md`
- `RELEASES.md`

## 检查清单

在更新 CHANGELOG 时，确保：

- [ ] 遵循 Keep a Changelog 规范的结构
- [ ] 使用具体的描述，避免模糊的"修复 bug"类表达
- [ ] 包含版本号和发布日期
- [ ] 破坏性变更（Breaking Changes）明确标注
- [ ] 按时间倒序排列（最新版本在最上方）
- [ ] 语义化版本号（Major.Minor.Patch）
