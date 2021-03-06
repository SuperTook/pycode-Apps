# TODO 改善发音效果
import os
import time
import sys
import winsound

DEFAULT_DURATION = 300
tone = {'a': 245, 'b': 285, 'c': 300, 'd': 342, 'e': 386, 'f': 413, 'g': 469,
        '1': 532, '2': 588, '3': 660, '4': 698, '5': 784, '6': 880, '7': 988,
        '!': 1080, '@': 1172, '#': 1302, '$': 1473, '%': 1532, '^': 1622, '&': 1800}


def _play(arg, duration=DEFAULT_DURATION):
    last = None
    for x in arg:
        if x in tone.keys():
            winsound.Beep(tone[x], duration)
            time.sleep(0.15)
            last = tone[x]
        elif x == '-':
            if last is not None:
                winsound.Beep(last, 100)
                time.sleep(0.15)
        elif x == '0':
            time.sleep(duration / 1000)
        elif x == "'":
            time.sleep(0.3)
        elif x == "|":
            time.sleep(0.08)
        elif x == '[':
            duration //= 2
        elif x == ']':
            duration *= 2


last_ = None
dur = DEFAULT_DURATION
print('退出：`',
      '低1:g',
      '低2:f',
      '低3:e',
      '低4:d',
      '低5:c',
      '低6:b',
      '低7:a',
      '',
      '原1:1',
      '原2:2',
      '原3:3',
      '原4:4',
      '原5:5',
      '原6:6',
      '原7:7',
      '',
      '高音：按住[Shift]+[音阶] (如 [shift]+[2] = @, @即为 高音2)',
      '下划线：用方括号括住, 括几次就几道线',
      '注：',
      '可输入多个音节',
      '输入 ~ + 文件名及路径(无后缀) 可保存上一次的简谱',
      '输入 . + 文件名及路径(含后缀) 可播放简谱', sep='\n')
while True:
    s = input('In：')
    if s.startswith('~'):
        with open(f'msc/{s.strip("~")}.beep', 'w', encoding='utf-8') as f:
            f.write(last_ if last_ is not None else 'a b c d e f g - | 1 2 3 4 5 6 7 - | ! @ # $ % ^ & - |')
    elif s == '`':
        break
    elif s.startswith('.') and s[1:].split() and os.path.exists(s[1:]):
        with open(s[1:], encoding='utf-8') as f:
            i = f.read().strip(' ')
            for _ in range(6):
                sys.stdout.write(f'加载中{"."*_}\r')
                time.sleep(0.01)
            _play(i, dur)
    else:
        _play(s, dur)
