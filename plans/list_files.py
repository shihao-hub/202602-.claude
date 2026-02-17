#!/usr/bin/env python3
"""
列出当前目录的所有文件名和文件数量
"""

import os


def list_files():
    """列出当前目录的所有文件名和文件数量"""
    # 获取当前目录
    current_dir = os.getcwd()

    # 获取当前目录下的所有条目
    entries = os.listdir(current_dir)

    # 过滤出文件（排除目录）
    files = [f for f in entries if os.path.isfile(os.path.join(current_dir, f))]

    # 打印文件数量
    print(f"当前目录: {current_dir}")
    print(f"文件数量: {len(files)}")
    print("-" * 50)
    print("文件列表:")

    # 打印所有文件名
    for file in files:
        print(f"  - {file}")


if __name__ == "__main__":
    list_files()
