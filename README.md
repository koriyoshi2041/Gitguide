# Git Journal

一个简单的命令行日记应用，专为学习Git版本控制系统而设计。

## 项目概述

Git Journal是一个基础的命令行工具，允许用户通过简单的文本界面创建、查看和搜索日记条目。每个日记都存储为独立的文本文件，按日期命名。

这个项目的主要目的不是作为一个功能齐全的日记应用，而是提供一个实用的环境来学习和练习Git版本控制系统的各种操作。通过管理你的日记内容，你可以自然地学习Git的基本概念和工作流程。

## 当前功能

- **基本日记操作**
  - 创建/更新日记条目
  - 查看指定日期的日记
  - 列出所有已有的日记
  - 按关键词搜索日记内容

- **Git学习辅助**
  - 每个操作后提供Git命令提示
  - 支持在不同分支记录不同类型的日记
  - 便于练习分支、合并和冲突解决

## 安装与使用

### 系统要求

- Python 3.6+
- Git

### 获取代码

```bash
git clone <仓库地址>
cd git-journal
```

### 使用方法

```bash
# 显示帮助信息
python journal.py help

# 创建或更新今天的日记
python journal.py write

# 查看指定日期的日记
python journal.py view

# 搜索日记内容
python journal.py search

# 列出所有日记
python journal.py list
```

## Git学习目标

通过使用Git Journal，你可以练习以下Git操作：

- **基础命令**：`git init`, `git add`, `git commit`, `git status`, `git log`
- **分支操作**：`git branch`, `git checkout/switch`, `git merge`
- **历史与差异**：`git diff`, `git log --graph`
- **回滚操作**：`git reset`, `git revert`
- **冲突解决**：在不同分支修改同一天的日记并尝试合并

## 项目结构

```
/git-journal/
├── journal.py            # 主程序脚本
├── README.md             # 项目说明文档
├── Git学习指南.md         # 零基础Git学习指南
├── Git工作流程实践指南.md  # VibeCoding Git工作流实践
└── entries/              # 日记条目存储目录
```

## 限制与不足

- 这是一个学习项目，不适合作为正式的日记应用使用
- 没有加密功能，所有日记都是明文存储
- 界面简单，只有基本的命令行交互
- 没有高级的搜索和组织功能

## 学习资源

项目包含两个学习指南文档：

1. **Git学习指南.md**：面向零基础用户的Git入门教程
2. **Git工作流程实践指南.md**：如何在日记项目中应用VibeCoding Git工作流

## 贡献与开发

这个项目主要用于学习目的，欢迎通过以下方式贡献：

- 添加新的日记功能
- 改进命令行界面
- 添加更多Git学习指南
- 修复bug和改进代码质量

## 许可证

MIT 