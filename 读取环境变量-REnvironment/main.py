#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： C.zf
# 开发人员 ： C.Z.F
# 开发时间 ： 2020/8/14 14:51
# 文件名称 ： getEnv.py
# 开发工具 ： PyCharm
import os
import time

environ = dict(os.environ)


def get_env():
    for k, v in environ.items():
        print('{:s}:'.format(k))
        for vv in v.split(';'):
            print('\t{:s}'.format(vv))
            time.sleep(0.01)
        print()
        time.sleep(0.01)


def find_env():
    condition = input('需要查找的环境变量（内容或变量名）：')
    for k, v in environ.items():
        for vv in v.split(';'):
            if vv == condition:
                print('In {:s} : {:s}'.format(k, vv))
            elif k == condition:
                print(k)
            time.sleep(0.01)


def m_find_env():
    condition = input('需要模糊查找的环境变量（内容或变量名）：')
    prints = []
    for k, v in environ.items():
        for vv in v.split(';'):
            if (condition in vv or condition.upper() in vv or
                    condition.title() in vv or condition.lower() in vv):
                prints.append('In {:s} : {:s}'.format(k, vv))

            elif (condition in k or condition.upper() in k or
                    condition.title() in k or condition.lower() in k):
                prints.append(k)
    for i in prints:
        if i.startswith('In'):
            print(i)
            time.sleep(0.01)

    for i in prints:
        if not i.startswith('In'):
            print(i)
            time.sleep(0.01)


def get_env_content():
    condition = input('需要获取内容的环境变量名：')
    for k, v in environ.items():
        if k == condition:
            print('{:s}:'.format(k))
            for vv in v.split(';'):
                print('\t{:s}'.format(vv))
                time.sleep(0.01)
            time.sleep(0.01)
            return


m = None
while m != '0':
    m = input('选项：0.退出；\n1.获取全部环境变量；2.寻找环境变量；\n3.模糊查询环境变量；4.获取变量内容 >>>')
    if m == '1':
        get_env()
    elif m == '2':
        find_env()
    elif m == '3':
        m_find_env()
    elif m == '4':
        get_env_content()
    print()
