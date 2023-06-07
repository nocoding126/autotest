"""
!/usr/bin/env python
# -*- coding: utf-8 -*-
@Time    : 2023/6/6 21:44
@Author  : 派大星
@Site    : 
@File    : setup.py
@Software: PyCharm
@desc:
"""
from tools.count_cases import count_cases, count_cases_num
from tools.util import write_excel

if __name__ == '__main__':

    count_cases_num()
    cases_list = count_cases()
    write_excel(cases_list)
