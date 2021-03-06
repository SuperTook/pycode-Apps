#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# Copyright (C) 2020 Chen Zhangfu, All Rights Reserved.
import re
import os
import qrcode
from pyzbar import pyzbar
from PIL import Image, ImageEnhance


def en_qr():
    dc = {'0': 'black', '1': 'red', '2': 'green', '3': 'blue', '4': 'purple'}
    s = input('二维码包含的网址：')
    c = input('颜色(0.黑白 1.红 2.绿 3.黄 4.紫)：')
    p = input('logo路径(不输入视为不添加logo)：')
    f = input('保存图片名（不含后缀）：')
    if re.match(r'(https://(\w*/)*)|(http://(\w*/)*)', s) is None:
        print('输入的不是网址')
        return
    if int(c) not in [0, 1, 2, 3, 4]:
        print('无此颜色')
        return

    if p == '':
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=3,
        )
        qr.add_data(s)
        qr.make(fit=True)
        img = qr.make_image(fill_color=dc[c], back_color='white')
        img.save(os.path.join('.', 'resQRCode', '{:s}.png'.format(f)))
    else:
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=8,
            border=4,
        )
        qr.add_data(s)
        qr.make(fit=True)

        img = qr.make_image(fill_color=dc[c], back_color='white')
        img = img.convert("RGBA")

        icon = Image.open(p)

        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        img.save(os.path.join('.', 'resQRCode', '{:s}.png'.format(f)))
    print('完成')


def de_qr():
    def __de_qr(n, qr_name):
        img = Image.open(qr_name)
        img = ImageEnhance.Brightness(img).enhance(2.0)  # 增亮
        img = ImageEnhance.Sharpness(img).enhance(17.0)  # 锐化
        img = ImageEnhance.Contrast(img).enhance(4.0)    # 增加对比度

        qrcodes = pyzbar.decode(img)
        for q in qrcodes:
            print(n, end='：')
            print(q.data.decode('utf-8'))

    path = input('输入二维码存放路径<批量转换>：')
    list_path = os.listdir(path)
    for i in range(len(list_path)):
        fpath = os.path.join(path, list_path[i])
        ftype = os.path.splitext(list_path[i])[1]

        if not os.path.isfile(fpath):
            continue
        if ftype in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif']:
            __de_qr(list_path[i], fpath)


m = input('1.生成 2.识别：')
if m == '1':
    en_qr()
elif m == '2':
    de_qr()
