#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： C.zf
# 开发人员 ： C.Z.F
# 开发时间 ： 2020/8/13 16:53
# 文件名称 ： system.py
# 开发工具 ： PyCharm
import os
import sys


def run_py(py_file, *run_args):
    r_args = ' '.join(run_args)
    command = 'python {:s} {:s}'.format(py_file, r_args)
    os.system(command)


def get_env():
    environ = dict(os.environ)
    for k, v in environ.items():
        v = v.split(';')
        environ[k] = v
    return environ
