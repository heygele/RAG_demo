# Git 上手指南 — 从零上传项目到 GitHub

## 一、配置 Git（只需做一次）

```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你注册GitHub用的邮箱"
```

## 二、在 GitHub 上创建空仓库

1. 打开 https://github.com，登录
2. 点右上角 **+** → **New repository**
3. 填仓库名（如 `RAG_demo`）
4. **不要勾** "Initialize this repository with a README"
5. 点 **Create repository**

记下页面显示的仓库地址，如：`https://github.com/你的用户名/RAG_demo.git`

## 三、上传本地项目到 GitHub

在 PyCharm 的 Terminal 中（或命令行 cd 到项目目录），逐条执行：

```bash
# 1. 初始化 Git 仓库
git init

# 2. 添加所有文件到暂存区
git add .

# 3. 首次提交
git commit -m "初始提交：RAG demo 项目"

# 4. 关联远程仓库（用你的仓库地址替换）
git remote add origin https://github.com/你的用户名/RAG_demo.git

# 5. 推送到 GitHub
git push -u origin main
```

> 如果第 5 步提示 `failed to push` 说明默认分支是 `master`，改成：
> `git push -u origin master`

推送时会弹窗让你登录 GitHub 账号认证。

## 四、日常同步流程

### 提交修改

```bash
git add .               # 暂存所有改动
git commit -m "改了什么内容"  # 提交
git push                # 推送到 GitHub
```

### 查看状态（随时用）

```bash
git status   # 查看当前改了哪些文件
git diff     # 查看具体改了什么内容
```

## 五、PyCharm 可视化操作（不用记命令）

| 操作 | 快捷键/方式 |
|---|---|
| 提交代码 | `Ctrl + K` → 勾选文件 → 写 commit message → Commit |
| 推送到 GitHub | `Ctrl + Shift + K` → Push |
| 查看文件状态 | 右侧边栏 **Commit** 标签页 |
| 查看修改历史 | 右键文件 → Git → Show History |

## 六、常用 Git 命令速查

| 命令 | 作用 |
|---|---|
| `git status` | 查看工作区状态 |
| `git add <文件>` | 暂存指定文件 |
| `git add .` | 暂存所有改动 |
| `git commit -m "消息"` | 提交暂存的内容 |
| `git push` | 推送到远程仓库 |
| `git pull` | 拉取远程最新代码 |
| `git log` | 查看提交历史 |
| `git diff` | 查看未暂存的改动 |

## 七、常见问题

- **推送时要求登录**：GitHub 会弹出浏览器或登录框，按提示登录即可
- **提示 `nothing to commit`**：说明没有未提交的改动，或者忘了 `git add`
- **`push` 被拒绝**：可能远程有新的提交，先 `git pull` 再重新 `push`
