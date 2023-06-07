"""
!/usr/bin/env python
# -*- coding: utf-8 -*-
@Time    : 2023/6/6 21:46
@Author  : 派大星
@Site    : 
@File    : util.py
@Software: PyCharm
@desc:
"""
import os
import openpyxl


def get_py_file_path(file_name='testcases'):
    """获取所有py文件的路径"""
    ROOT_FILE_DIR = os.path.dirname(os.path.dirname(__file__))  # 获取项目的路径
    TESTCASE_DIR = os.path.join(ROOT_FILE_DIR, file_name)  # 获取testcases目录的路径
    # 获取testcases目录下的所有文件
    files_path = []
    for _root, _dirs, _files in os.walk(TESTCASE_DIR):
        for _file in _files:
            if _file.endswith('.py') and _file != '__init__.py':
                file_path = os.path.join(_root, _file)
                files_path.append(file_path)
    return files_path


def write_excel(data):
    """将数据写入excel"""
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '测试用例'
    for row in data:
        sheet.append(row)
    wb.save('testcases.xlsx')


def snake_to_camel(snake_str):
    """蛇型命名转为驼峰命名"""
    if not snake_str:
        return snake_str
    elif snake_str.endswith('_implement.py'):
        snake_str = snake_str[:-13]
    else:
        snake_str = snake_str[:-3]
    camel_res = snake_str[0].upper()

    flag = False
    for letter in snake_str[1:]:
        if letter == '_':
            flag = True
            continue
        camel_res += letter.upper() if flag else letter
        flag = False
    return camel_res


if __name__ == '__main__':
    files_path = get_py_file_path('testcases_001')
    print(files_path)
