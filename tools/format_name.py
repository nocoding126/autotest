"""
!/usr/bin/env python
# -*- coding: utf-8 -*-
@Time    : 2023/6/7 11:51
@Author  : 派大星
@Site    : 
@File    : format_name.py
@Software: PyCharm
@desc:
"""
import os
import importlib
import inspect
from tools.util import get_py_file_path, snake_to_camel


ROOT_FILE_DIR = os.path.dirname(os.path.dirname(__file__))  # 获取项目的路径


def format_class_name():
    """格式化类名
    由脚本名（蛇型命名）转为类命名（大驼峰法）
    """
    files_path = get_py_file_path('testcases')
    for _file_path in files_path:
        testcases_file_path = _file_path.replace(ROOT_FILE_DIR, '')
        module_path = testcases_file_path.strip('.py').strip('/').replace('/', '.')  # 获取模块的路径
        module_name = testcases_file_path.split('/')[-1]
        print('模块名称', module_name)
        try:
            test_module = importlib.import_module(module_path)  # 导入模块
        except ModuleNotFoundError:
            print('导入模块失败,未找到', module_path)
            continue

        for name, obj in inspect.getmembers(test_module, inspect.isclass):
            if name == 'TestCase':
                continue
            # print(name, obj)
            snake_str = snake_to_camel(module_name)
            print(snake_str)
            print(_file_path)
            # with open(_file_path, 'r+', encoding='utf-8') as f:
            #     lines = f.readlines()
            #     print(lines)
            #     break
            # if name == module_name[:-3]:
            #     continue
            # else:
            #     print('重命名成功！')


def comment_script_name():
    """根据用例状态，标注出未完成的脚本"""
    files_path = get_py_file_path('testcases')
    for _file_path in files_path:
        testcases_file_path = _file_path.replace(ROOT_FILE_DIR, '')
        module_path = testcases_file_path.strip('.py').strip('/').replace('/', '.')  # 获取模块的路径
        try:
            test_module = importlib.import_module(module_path)  # 导入模块
        except ModuleNotFoundError:
            print('导入模块失败,未找到', module_path)
            continue

        for name, obj in inspect.getmembers(test_module, inspect.isclass):
            if name == 'TestCase':
                continue
            test_case_status = getattr(obj, 'status', None)
            if test_case_status == 'Implement' and not testcases_file_path.endswith('_implement.py'):
                os.rename(_file_path, _file_path[:-3] + '_implement.py')
                print('重命名成功！')


if __name__ == '__main__':
    format_class_name()
