# Git工作流程实践指南：在日记系统中练习VibeCoding工作流

本文档详细描述如何在我们的Git Journal日记系统中实践"VibeCoding Git工作流"——一种在与AI协作或进行代码实验时保持代码库整洁的方法论。

## 什么是VibeCoding Git工作流？

VibeCoding Git工作流的核心思想是：**在使用具有不确定性的工具（如AI）修改代码时，要最大限度地利用版本控制系统（Git）来保护你的工作进度，并保持代码历史的清晰。**

关键概念：
- 将Git作为你的"救生索"
- 在干净的代码库状态基础上进行实验
- 发现问题时果断回滚（git reset --hard HEAD）
- 避免在错误代码上层层叠加修复

## 在日记系统中实践这一工作流

我们的Git Journal日记应用提供了一个理想的环境来练习这种工作流。下面是如何将VibeCoding Git工作流应用到日记项目中的具体步骤：

### 一、基础准备：创建实验分支

1. 确保主分支（master/main）处于干净状态：
   ```bash
   git status
   # 确认显示"nothing to commit, working tree clean"
   ```

2. 创建一个实验分支，用于尝试新功能或AI建议：
   ```bash
   git branch experiment-feature
   git checkout experiment-feature
   # 或使用新命令：git switch experiment-feature
   ```

### 二、在日记系统中模拟AI协作场景

#### 场景一：修改日记格式

1. **准备阶段：确保代码库干净**
   ```bash
   git status
   # 确认显示"nothing to commit, working tree clean"
   ```

2. **尝试"AI修改"（手动模拟）**：
   - 修改已有的日记文件，添加新的格式（例如，添加心情评分，天气记录等）
   - 或者修改`journal.py`脚本，让它支持新的格式化选项

3. **审查阶段**：
   ```bash
   git diff
   # 仔细检查所有修改
   ```

4. **决策阶段**：
   - 如果修改符合预期：
     ```bash
     git add .
     git commit -m "增强日记格式，添加心情和天气记录功能"
     ```
   - 如果修改不符合预期或导致程序错误：
     ```bash
     git reset --hard HEAD
     # 所有修改立即被撤销，回到干净状态
     ```

#### 场景二：添加搜索功能

1. **准备阶段**：
   ```bash
   git status
   # 确保当前工作区干净
   ```

2. **尝试"AI修改"**：
   - 在`journal.py`中添加搜索功能，允许按关键词搜索日记内容

3. **审查修改**：
   ```bash
   git diff
   # 详细检查修改的代码
   ```

4. **决策**：
   - 如果搜索功能正常工作：提交保存
   - 如果代码有问题：回滚，重新尝试

### 三、高级模拟：故意创造冲突情况

要真正体验Git在解决冲突方面的能力，可以尝试以下练习：

1. 在主分支上修改某天的日记：
   ```bash
   git checkout master
   # 编辑entries/YYYY-MM-DD.txt
   git add entries/YYYY-MM-DD.txt
   git commit -m "在主分支修改日记内容"
   ```

2. 切换到实验分支，修改同一天的日记内容但内容不同：
   ```bash
   git checkout experiment-feature
   # 编辑同一个entries/YYYY-MM-DD.txt文件
   git add entries/YYYY-MM-DD.txt
   git commit -m "在实验分支修改日记内容"
   ```

3. 尝试合并，会出现冲突：
   ```bash
   git checkout master
   git merge experiment-feature
   # 这会产生冲突
   ```

4. 解决冲突的两种方式：
   - 手动编辑冲突文件，然后提交解决方案
   - 或者放弃合并，使用回滚命令：
     ```bash
     git merge --abort
     ```

### 四、VibeCoding工作流的日常练习

在使用Git Journal时，养成以下习惯来练习VibeCoding工作流：

1. **频繁提交**：每写完一篇完整的日记就提交一次
   ```bash
   git add entries/YYYY-MM-DD.txt
   git commit -m "添加今天的日记"
   ```

2. **先提交，再实验**：想尝试新格式或功能前，确保当前工作已提交

3. **使用分支进行主题隔离**：
   - `personal`分支存放个人日记
   - `work`分支存放工作日记
   - `experiment`分支尝试新功能

4. **善用回滚命令**：不要害怕使用`git reset --hard HEAD`，它是你的救生索

5. **保持历史清晰**：每次提交应当有明确目的，提交消息应当清晰描述改动

## 实践练习计划

以下是一个7天的练习计划，帮助你在Git Journal中掌握VibeCoding工作流：

### 第1天：基本工作流
- 创建一篇日记并提交
- 修改日记并提交
- 查看历史记录

### 第2天：分支操作
- 创建个人日记分支
- 在不同分支记录不同主题的日记
- 练习分支切换

### 第3天：合并与冲突
- 故意在两个分支上修改同一天的日记
- 尝试合并并解决冲突
- 尝试放弃合并

### 第4天：回滚操作
- 在日记中做一些实验性修改
- 使用`git reset --hard HEAD`回滚
- 尝试更温和的回滚方式：`git reset --soft HEAD^`

### 第5天：日记功能增强
- 在一个实验分支上修改`journal.py`添加新功能
- 测试功能，决定是提交还是回滚
- 如果功能可用，将实验分支合并到主分支

### 第6天：模拟协作
- 创建两个不同的工作目录（模拟两个开发者）
- 在两个目录中同时修改日记系统
- 尝试合并两边的修改

### 第7天：工作流程整合
- 练习完整的工作流程：创建分支 -> 修改 -> 测试 -> 决策（提交/回滚）-> 合并
- 回顾所学内容，整理个人Git工作流程笔记

## 小贴士

- **永远不要害怕回滚**：Git的强大之处在于它允许你随时回到已知的良好状态
- **提交前先测试**：确保修改是有效的再提交
- **提交消息要有意义**：它们是你未来理解历史的线索
- **把每次实验当作学习机会**：即使失败了需要回滚，你也从中学到了什么不起作用

通过在Git Journal中实践这些练习，你不仅能学习Git的技术细节，还能掌握一种保持代码库整洁、避免在错误上积累的工作哲学，这在与AI工具协作或进行任何软件开发时都极为宝贵。 