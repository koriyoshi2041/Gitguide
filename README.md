# Git Journal

一个简单的命令行日记应用，专为学习Git版本控制系统而设计。

## 项目概述

Git Journal是一个简单的命令行工具，允许用户创建和查看每日文本日记条目。每个日记条目都存储在一个独立的文件中，按日期命名。

这个项目的主要目的是作为一个载体来学习Git的各种操作，通过实际使用Git来管理你的日记内容，从而学习版本控制的概念和操作。

## 特性

- 创建和更新日记条目
- 查看指定日期的日记
- 列出所有已有的日记
- 集成Git操作提示，帮助学习Git命令

## 安装与使用

### 前提条件

- Python 3.6+
- Git

### 获取代码

```bash
git clone <仓库地址>
cd git-journal
```

### 使用方法

```bash
# 写新日记或更新今天的日记
./journal.py write

# 查看指定日期的日记
./journal.py view

# 列出所有日记
./journal.py list

# 显示帮助信息
./journal.py help
```

## Git学习目标

通过使用Git Journal，你可以学习以下Git操作：

- `git init`：初始化仓库
- `git add`：将修改的文件添加到暂存区
- `git commit`：提交更改
- `git status`：查看工作区状态
- `git log`：查看提交历史
- `git diff`：查看文件变化
- `git branch`：创建和管理分支
- `git checkout/switch`：切换分支
- `git merge`：合并分支
- 解决合并冲突
- `git remote`、`git push`、`git pull`：与远程仓库交互

## 学习建议

1. 每完成一个日记就提交一次代码
2. 尝试创建不同主题的日记分支（如"工作日记"、"个人日记"）
3. 故意在不同分支上修改同一天的日记，然后尝试合并
4. 使用`git log --graph`查看你的提交历史

## 项目扩展（可选）

如果你想进一步扩展这个项目，可以考虑添加以下功能：

- 日记标签功能
- 搜索日记内容
- 文本编辑器集成
- 远程备份功能

## 许可证

MIT 