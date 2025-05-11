#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Git Journal - 一个简单的命令行日记应用
用于学习Git版本控制系统
"""

import os
import sys
import datetime
from pathlib import Path

# 定义常量
ENTRIES_DIR = "entries"

def ensure_entries_dir():
    """确保日记条目目录存在"""
    if not os.path.exists(ENTRIES_DIR):
        os.makedirs(ENTRIES_DIR)
        print(f"创建日记目录: {ENTRIES_DIR}")

def write_entry():
    """写入今天的日记条目"""
    today = datetime.date.today()
    filename = f"{today.strftime('%Y-%m-%d')}.txt"
    filepath = os.path.join(ENTRIES_DIR, filename)
    
    # 检查文件是否已存在
    file_exists = os.path.exists(filepath)
    
    # 打开文件进行写入
    print("请输入今天的日记内容，输入空行并回车结束：")
    content = []
    while True:
        line = input()
        if not line:
            break
        content.append(line)
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    action = "更新" if file_exists else "创建"
    print(f"日记已{action}到 {filepath}")
    print("提示: 使用以下Git命令保存你的日记")
    print(f"  git add {filepath}")
    print(f"  git commit -m \"日记: {today.strftime('%Y-%m-%d')}\"")

def view_entry():
    """查看指定日期的日记条目"""
    while True:
        date_input = input("请输入要查看的日记日期 (YYYY-MM-DD)，或输入 'list' 查看所有日期: ")
        
        if date_input.lower() == 'list':
            list_entries()
            continue
            
        try:
            # 验证日期格式
            datetime.datetime.strptime(date_input, '%Y-%m-%d')
            filename = f"{date_input}.txt"
            filepath = os.path.join(ENTRIES_DIR, filename)
            
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"\n===== {date_input} 的日记 =====")
                    print(content)
                    print("========================")
                    print("提示: 使用以下Git命令查看此文件的历史")
                    print(f"  git log {filepath}")
                    print(f"  git diff <commit1> <commit2> -- {filepath}")
                break
            else:
                print(f"找不到{date_input}的日记，请重新输入或输入'list'查看可用日期")
        except ValueError:
            print("日期格式无效，请使用YYYY-MM-DD格式")

def search_entries():
    """搜索日记内容"""
    keyword = input("请输入要搜索的关键词: ")
    if not keyword:
        print("搜索关键词不能为空")
        return
    
    ensure_entries_dir()
    entries = [f for f in os.listdir(ENTRIES_DIR) if f.endswith('.txt')]
    
    if not entries:
        print("目前还没有日记条目可供搜索。")
        return
    
    found = False
    print(f"\n搜索关键词 '{keyword}' 的结果:")
    
    for entry in sorted(entries):
        date = entry.replace('.txt', '')
        filepath = os.path.join(ENTRIES_DIR, entry)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if keyword.lower() in content.lower():
                found = True
                print(f"\n- {date}:")
                
                # 找出包含关键词的行并显示
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if keyword.lower() in line.lower():
                        print(f"  行 {i+1}: {line}")
    
    if not found:
        print("没有找到包含该关键词的日记。")
    else:
        print("\n提示: 使用 'view' 命令查看完整日记内容")

def list_entries():
    """列出所有日记条目"""
    ensure_entries_dir()
    entries = [f for f in os.listdir(ENTRIES_DIR) if f.endswith('.txt')]
    
    if not entries:
        print("目前还没有日记条目。使用'write'命令创建你的第一篇日记！")
        return
    
    print("\n可用的日记日期:")
    for entry in sorted(entries):
        date = entry.replace('.txt', '')
        print(f"  {date}")
    print()

def show_help():
    """显示帮助信息"""
    print("""
Git Journal - 简单的命令行日记应用

使用方法:
  python journal.py <命令>

可用命令:
  write    创建或更新今天的日记
  view     查看指定日期的日记
  search   搜索日记内容
  list     列出所有已有的日记日期
  help     显示此帮助信息

示例:
  python journal.py write    # 写入今天的日记
  python journal.py view     # 查看指定日期的日记
  python journal.py search   # 搜索日记内容
  python journal.py list     # 列出所有日记
    """)

def main():
    """主函数"""
    ensure_entries_dir()
    
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'write':
        write_entry()
    elif command == 'view':
        view_entry()
    elif command == 'search':
        search_entries()
    elif command == 'list':
        list_entries()
    elif command in ['help', '-h', '--help']:
        show_help()
    else:
        print(f"未知命令: {command}")
        show_help()

if __name__ == "__main__":
    main() 