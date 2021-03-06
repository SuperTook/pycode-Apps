#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： C.zf
# 开发人员 ： C.Z.F
# 开发时间 ： 2020/7/5 15:53
# 文件名称 ： Cmd.py
# 开发工具 ： PyCharm
import math
import sys
import time
import hmac
import types
from xpinyin import Pinyin


def clock_list():
    """
    获取当前时间，返回列表
    :return: <list[str]> ["年-月-日", "时:分:秒", "AM/PM", "上午x点/下午x点", "星期几",
                          "此年中的第几天", "此年中的第几周(如果第一周不满7天，第一周不算)"]
    """
    now = time.strftime
    clk = [now('%Y-%m-%d'), now('%H:%M:%S'), now('%p'), now('%I'), now('%A'), now('%j'), now('%U')]
    return clk


def clock_str():
    """
    获取当前时间，返回字符串
    :return: <str> "年-月-日 时:分:秒"
    """
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    return now


def load_a(trns, title='请稍等,精彩马上呈现'):
    """
    在控制台上输出loading的文字
    :param trns: 次数
    :param title: 前面的文字
    :return: None
    """
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(title)

    for foo in range(trns):
        sys.stdout.write('—')

        time.sleep(0.25)
        sys.stdout.write('\b')
        sys.stdout.write('\\')

        time.sleep(0.25)
        sys.stdout.write('\b')
        sys.stdout.write('|')

        time.sleep(0.25)
        sys.stdout.write('\b')
        sys.stdout.write('/')

        time.sleep(0.25)
        sys.stdout.write('\b')


def load_b(trns, title='请稍等,精彩马上呈现'):
    """
    在控制台上输出loading的文字
    :param trns: 次数
    :param title: 前面的文字
    :return: None
    """
    sys.stdout.write('\r')
    sys.stdout.flush()

    for foo in range(trns):
        sys.stdout.write(title)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write(' ')
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('.')

        time.sleep(0.25)
        sys.stdout.write('\r')


def draw_par(speed, angle, miles, par_char='O'):
    """
    预测抛物线
    :param speed: 速度
    :param angle: 角度
    :param miles: 英里
    :param par_char: 描述抛物线的字符 (默认为 O (字母O))
    :return: None
    """

    for x in range(miles + 1):
        ws_num = math.floor(0.5 + x * math.tan(speed) - x * x / (angle * math.cos(speed)))
        print('%04d' % x, ' ' * ws_num + par_char, sep='')


def limit_line_print(string, clo):
    """
    限制每行的输出量
    :param string: 要输出的字符串
    :param clo: 输出量
    :return: None
    """
    x = 0
    for item in string:
        print(item, end='')
        x += 1
        if x % clo == 0:
            print('\n', end='')


def inv(obj):
    """
    颠倒字符串
    :param obj: 需要颠倒的
    :return: <list>
    """
    obj = str(obj)
    res = obj[::-1]
    return res


def en_md5(s, coding, hash_key):
    s = s.encode(coding)
    key = hash_key.encode(coding)
    h = hmac.new(key, s, digestmod='MD5')
    return h.hexdigest()


def en_sha1(s, coding, hash_key):
    s = s.encode(coding)
    key = hash_key.encode(coding)
    h = hmac.new(key, s, digestmod='SHA1')
    return h.hexdigest()


def en_sha256(s, coding, hash_key):
    s = s.encode(coding)
    key = hash_key.encode(coding)
    h = hmac.new(key, s, digestmod='SHA256')
    return h.hexdigest()


def en_sha512(s, coding, hash_key):
    s = s.encode(coding)
    key = hash_key.encode(coding)
    h = hmac.new(key, s, digestmod='SHA512')
    return h.hexdigest()


def sort_chinese_list(words, reverse=False):
    """
    对汉字列表排序（音序法）
    :param words: 需要排序的汉字列表
    :param reverse: 正序赋值False，倒序赋值True
    :return: <list> [排序后的列表]
    """
    pinyin = Pinyin()

    temp = []
    for item in words:
        temp.append((pinyin.get_pinyin(item), item))
    temp.sort(reverse=reverse)

    rtn = []
    for i in range(len(temp)):
        rtn.append(temp[i][1])
    return rtn


def location_code(words, sep=' '):
    """
    获取汉字的区位码
    :param words: 需要获取区位码的汉字字符串
    :param sep: 分隔符
    :return: <str> 区位码
    """
    tmp = []

    for w in words:
        gbk = w.encode('gbk')
        code = '{0:02d}'.format((gbk[0] - 160)) + '{0:02d}'.format((gbk[1] - 160))
        tmp.append(code)

    rtn = sep.join(tmp)
    return rtn


def get_pinyin(words):
    """
    获取汉字字符串每个汉字的拼音
    :param words: 汉字字符串
    :return: <dict> ""
    """
    pinyin = Pinyin()
    p = pinyin.get_pinyin(words, splitter=' ')
    p = p.split()
    rtn = dict(zip(words, p))
    return rtn


# -----------------------------------
__all__ = [k for k, v in globals().items() if isinstance(v, types.FunctionType)]
