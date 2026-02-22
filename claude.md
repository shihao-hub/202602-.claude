我希望你在每次修改后，请自动用 Git 提交。规则如下：

1. 禁止嵌套 Git：若当前目录或任意父目录已存在 .git，则直接提交，不得初始化。
2. 未被 Git 管理时（路径上无任何 .git）：
   - 执行 `git init`
   - 创建基本 `.gitignore`
3. 提交格式：

    ```markdown
    **格式**：  
    `<type>(<scope>): <subject>`（中文，≤50字，动词开头，无句号）  
    可选正文（说明“是什么”和“为什么”，每行≤72字符，用 `-` 列表）  
    可选页脚（如 `BREAKING CHANGE:` 或 `Closes #xxx`）
    
    **Type**：  
    `feat`（新功能）、`fix`（修复）、`docs`（文档）、`style`（格式）、`refactor`（重构）、`perf`（性能）、`test`、`chore`、`ci`、`revert`
    
    **Scope 示例**：  
    `creator`, `product`, `auth`, `db`, `api`, `metrics`, `submission` 等（多模块时可省略）
    
    **动词参考**：添加、修复、优化、重构、移除、更新、升级、集成
    
    **特殊**：  
    - 破坏性变更加 `!` 并在 footer 写 `BREAKING CHANGE: ...`  
    - 关联 issue 用 `Closes #xxx`
    ```

---

我希望你在每次修改后，更新项目的 README.md 文件（没有则创建）

---

我希望你在每次修改后，根据当前项目的结构，考虑是否需要更新 .gitignore 文件

---

我希望你尽量用中文回答问题

---

我希望你在 docs 目录中写入 markdown 文档时，采用 kebab-case（连字符分隔）的命名规范

---

我希望你可以自行判断关键回答，将其持久化为 docs 目录中的 md文档，以待未来使用（需要用户确认）

---

我希望你不要猜测用户意图，不懂就是不懂，信息不足请询问用户

---

我希望你可以自行判断是否需要对用户问题中的内容进行调研（需要用户确认）

---

我希望你在回答一些问题的时候，可以大胆探索自动化的可能

---

我希望你遇到`Error: Permission to use Bash with command`时，在整个回复结束后，全部列出来让我阅读

---