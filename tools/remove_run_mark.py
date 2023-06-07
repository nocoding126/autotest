"""
!/usr/bin/env python
# -*- coding: utf-8 -*-
@Time    : 2023/6/7 11:31
@Author  : 派大星
@Site    : 
@File    : remove_run_mark.py
@Software: PyCharm
@desc:
"""
import os
import re
from tools.util import get_py_file_path


def remove_run_mark(file_name='testcases_001'):
    """去除所有用例的运行标记"""
    files_path = get_py_file_path(file_name)
    if files_path:
        for file_path in files_path:
            if not re.findall(r'\w+.py', file_path):
                file_path_name = file_path[:-4] + '.py'
                os.rename(file_path, file_path_name)
                print('去除运行标记成功！')
    else:
        print('用例文件夹为空，无法去除运行标记！')


if __name__ == '__main__':
    remove_run_mark()
