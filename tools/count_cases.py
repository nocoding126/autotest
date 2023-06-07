"""
!/usr/bin/env python
# -*- coding: utf-8 -*-
@Time    : 2023/6/6 21:45
@Author  : 派大星
@Site    : 
@File    : count_cases.py
@Software: PyCharm
@desc:
"""
import importlib
import inspect
import os
from itertools import groupby
from tools.util import get_py_file_path
from tools.util import write_excel

ROOT_FILE_DIR = os.path.dirname(os.path.dirname(__file__))  # 获取项目的路径


def count_cases():
    """统计用例"""
    files_path = get_py_file_path()
    cases_list = []
    cases_title_list = ['用例名称（测试类名）', '标题（测试类描述）', '描述（desc属性）', '标签（tags）', '状态(status)',
                        '优先级 (priority)', '归属人(owner)', '模块(testcases下一级子目录)',
                        '子模块（模块下一级子目录）', '路径（相对于testcases的脚本路径或模块路径）', '步骤（步骤描述）']
    cases_list.append(cases_title_list)
    for _file_path in files_path:
        testcases_file_path = _file_path.replace(ROOT_FILE_DIR, '')
        module_path = testcases_file_path.strip('.py').strip('/').replace('/', '.')  # 获取模块的路径
        module_list = module_path.split('.')
        module_dir = module_list[1:2]  # 获取模块的目录
        sub_module_dir = module_list[2:3]  # 获取子模块的目录
        try:
            test_module = importlib.import_module(module_path)  # 导入模块
        except ModuleNotFoundError:
            print('导入模块失败,未找到', module_path)
            continue

        for name, obj in inspect.getmembers(test_module, inspect.isclass):
            if name == 'TestCase':
                continue
            test_case_name = name
            test_case_title = obj.__doc__
            test_case_desc = getattr(obj, 'desc', '')
            test_case_owner = getattr(obj, 'owner', '')
            test_case_priority = getattr(obj, 'priority', '')
            test_case_status = getattr(obj, 'status', '')
            test_tags = getattr(obj, 'tags', '')
            test_tags_list = list(test_tags)
            test_case_tags = ','.join(test_tags_list) if isinstance(test_tags_list, list) else test_tags
            step_desc = getattr(obj, 'run_test', '').__doc__ or ''
            cases_list.append([test_case_name, test_case_title, test_case_desc, test_case_tags, test_case_status,
                               test_case_priority, test_case_owner, module_dir, sub_module_dir, testcases_file_path,
                               step_desc])
    return cases_list


def count_cases_num(key='owner'):
    """统计用例数量"""
    cases_list = count_cases()[1:]
    if key == 'owner':
        cases_list.sort(key=lambda x: x[6])
        for name, group in groupby(cases_list, key=lambda x: x[6]):
            print(name, len(list(group)))
    else:
        cases_list.sort(key=lambda x: x[7])
        for name, group in groupby(cases_list, key=lambda x: x[7]):
            print(name, len(list(group)))


if __name__ == '__main__':
    # count_cases_num()
    # write_excel(count_cases())
    print(count_cases())
