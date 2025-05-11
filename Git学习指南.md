# Git 学习指南（零基础）

本指南面向完全没有Git使用经验的用户，帮助你通过Git Journal项目学习Git版本控制系统的基础知识和操作。

## 1. Git是什么？

Git是一个分布式版本控制系统，它可以跟踪你对文件所做的更改，让你能够：

- 记录文件的修改历史
- 恢复到之前的版本
- 并行开发不同功能
- 与他人协作处理同一项目
- 安全备份你的工作

简单来说，Git就像是一个超级强大的"保存历史记录"功能，它记录了你项目中每个文件的所有变化。

## 2. 准备工作

### 安装Git

在开始使用Git Journal之前，你需要先安装Git：

**Windows用户**：
- 下载并安装 [Git for Windows](https://gitforwindows.org/)
- 安装过程中选择默认选项即可

**Mac用户**：
- 打开终端，输入 `git --version`
- 如果没有安装，系统会提示你安装
- 或者通过Homebrew安装：`brew install git`

**Linux用户**：
- Debian/Ubuntu: `sudo apt-get install git`
- Fedora: `sudo dnf install git`

### 配置Git

安装完成后，需要进行基本配置：

1. 打开终端（Mac/Linux）或Git Bash（Windows）
2. 设置你的名字和邮箱（这些信息会出现在你的提交记录中）：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

## 3. Git核心概念

使用Git前，先了解几个核心概念：

- **仓库（Repository）**：存储项目所有文件和历史记录的地方
- **工作区（Working Directory）**：你当前编辑的文件所在的目录
- **暂存区（Staging Area）**：临时存储你准备提交的更改
- **提交（Commit）**：将暂存区的更改永久保存到仓库的历史记录
- **分支（Branch）**：独立的开发线，让你可以同时进行多个功能的开发

## 4. 使用Git Journal练习Git

Git Journal是一个简单的命令行日记应用，专为学习Git而设计。通过记录、修改和管理日记，你可以自然地学习Git的各种操作。

### 4.1 获取项目

1. 下载Git Journal项目代码到你的电脑
2. 或者，如果你想从零开始，可以按照以下步骤创建项目：

```bash
# 创建项目目录
mkdir git-journal
cd git-journal

# 初始化Git仓库
git init

# 创建日记目录
mkdir entries

# 下载journal.py脚本（或者你可以手动创建）
# ...
```

### 4.2 项目结构

```
/git-journal/              # 项目根目录
├── journal.py            # 主程序脚本
├── README.md            # 项目说明文档
└── entries/             # 日记条目存储目录
    └── .gitkeep         # 空文件，用来让Git跟踪空目录
```

### 4.3 使用流程

以下是使用Git Journal练习Git的基本流程：

#### 第一步：创建你的第一篇日记

1. 进入项目目录：
   ```bash
   cd git-journal
   ```

2. 运行写日记命令：
   ```bash
   python journal.py write
   ```

3. 输入日记内容，输入完成后按回车键并输入空行结束

4. 查看工作区状态：
   ```bash
   git status
   ```
   你会看到新创建的日记文件显示为"未跟踪文件"

5. 将日记添加到暂存区：
   ```bash
   git add entries/YYYY-MM-DD.txt  # 替换YYYY-MM-DD为实际日期
   ```

6. 提交你的日记：
   ```bash
   git commit -m "添加今天的日记"
   ```

#### 第二步：修改你的日记

1. 再次运行写日记命令修改今天的日记：
   ```bash
   python journal.py write
   ```

2. 查看你对日记做了哪些修改：
   ```bash
   git diff
   ```

3. 添加并提交修改：
   ```bash
   git add entries/YYYY-MM-DD.txt
   git commit -m "更新今天的日记"
   ```

#### 第三步：查看历史记录

查看你的提交历史：
```bash
git log
```

查看特定文件的历史：
```bash
git log entries/YYYY-MM-DD.txt
```

以图形方式查看历史：
```bash
git log --graph --oneline
```

#### 第四步：创建和使用分支

1. 创建一个新分支用于记录个人日记：
   ```bash
   git branch personal
   ```

2. 切换到新分支：
   ```bash
   git checkout personal
   # 或者使用新命令
   git switch personal
   ```

3. 在这个分支上创建个人日记：
   ```bash
   python journal.py write
   ```

4. 添加并提交：
   ```bash
   git add entries/YYYY-MM-DD.txt
   git commit -m "在个人分支添加日记"
   ```

5. 切换回主分支：
   ```bash
   git checkout master
   # 或
   git switch master
   ```

#### 第五步：合并分支

1. 在master分支上合并personal分支的内容：
   ```bash
   git merge personal
   ```

2. 如果出现冲突（你在两个分支修改了同一天的日记）：
   - 编辑冲突文件，决定保留哪些内容
   - 保存文件
   - 添加并提交解决方案：
     ```bash
     git add entries/YYYY-MM-DD.txt
     git commit -m "解决合并冲突"
     ```

## 5. Git命令速查表

### 基础命令

- `git init`：在当前目录创建新的Git仓库
- `git status`：查看工作区状态
- `git add <文件>`：将文件添加到暂存区
- `git commit -m "消息"`：提交暂存区的更改
- `git log`：查看提交历史
- `git diff`：查看工作区和暂存区的差异

### 分支操作

- `git branch`：列出所有本地分支
- `git branch <分支名>`：创建新分支
- `git checkout <分支名>` 或 `git switch <分支名>`：切换分支
- `git merge <分支名>`：将指定分支合并到当前分支
- `git branch -d <分支名>`：删除分支

### 远程仓库操作（进阶）

- `git remote add origin <URL>`：添加远程仓库
- `git push -u origin <分支名>`：推送到远程仓库
- `git pull`：从远程仓库拉取更新
- `git clone <URL>`：克隆远程仓库

## 6. 常见问题与解决方案

### 1. "fatal: not a git repository" 错误

这表示你不在Git仓库目录内。确保你已经进入git-journal目录，或者使用`git init`初始化仓库。

### 2. 提交时显示"nothing to commit"

这可能是因为你没有添加任何文件到暂存区。使用`git add`添加你修改的文件。

### 3. 合并冲突

当两个分支修改了同一个文件的同一部分时会发生冲突。Git会在文件中标记冲突区域：

```
<<<<<<< HEAD
当前分支的内容
=======
要合并的分支的内容
>>>>>>> branch-name
```

编辑文件，保留你想要的内容，删除标记符，然后提交解决方案。

## 7. 学习路径建议

1. **基础阶段**（1-2天）：
   - 创建和提交日记
   - 学习`git status`、`git add`、`git commit`、`git log`命令

2. **分支操作**（2-3天）：
   - 创建不同主题的日记分支
   - 在分支间切换
   - 合并分支

3. **历史操作**（1-2天）：
   - 查看文件的修改历史
   - 比较不同版本
   - 回退到之前版本

4. **协作模拟**（可选，2-3天）：
   - 设置远程仓库（GitHub/Gitee）
   - 推送和拉取更新
   - 模拟多人协作

## 8. 进阶学习资源

- [Git官方文档](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com/)
- [Pro Git书籍](https://git-scm.com/book/zh/v2)（免费在线阅读）
- [Git可视化学习](https://learngitbranching.js.org/?locale=zh_CN)

## 9. 小贴士

- 养成定期提交的习惯，每完成一个小功能就提交一次
- 编写清晰的提交消息，描述你做了什么更改
- 尝试故意创造冲突并解决它们，这是Git学习中非常重要的一课
- 使用`git help <命令>`获取任何命令的详细帮助信息

通过Git Journal项目学习Git是一个循序渐进的过程。不要急于一次学会所有内容，从基础操作开始，逐步探索更复杂的功能。祝你学习愉快！ 