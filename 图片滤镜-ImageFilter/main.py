#!usr/bin/env python
# coding=utf-8
# Copyright (c) Chen Zhangfu,
# all rights reserved.
from PIL import Image, ImageFilter


while True:
    m = int(input('0.退出\n1.模糊 2.轮廓 3.细节 4.锐化\n5.边界增强 6.浮雕 7.平滑\nInput：'))
    dm = {1: ImageFilter.BLUR, 2: ImageFilter.CONTOUR, 3: ImageFilter.DETAIL, 4: ImageFilter.SHARPEN,
          5: ImageFilter.EDGE_ENHANCE_MORE, 6: ImageFilter.EMBOSS, 7: ImageFilter.SMOOTH_MORE}
    if m not in dm.keys():
        continue
    if m == 0:
        break
    src = input('源文件存放路径（含文件名）：').replace('\\', '/')
    tar = input('保存至（输入不含后缀的文件名）：')

    img = Image.open(src)
    n_img = img.filter(dm[m])
    n_img.save('resImg/{:s}.png'.format(tar), 'png')
    print('完成', end='\n\n')
