#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： C.zf
# 开发人员 ： C.Z.F
# 开发时间 ： 2020/7/10 15:10
# 文件名称 ： Img.py
# 开发工具 ： PyCharm
import os
import types
import cv2
from PIL import Image
from MyQR import myqr
from pyzbar import pyzbar


def convert_type(path, new_path, new_name, flag):
    """
    转换图片类型
    :param path: 源图片路径
    :param new_path: 新图片保存路径 无图片名
    :param new_name: 新图片名称 无后缀
    :param flag: 类型
    :return: None
    """
    flag_list = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tif']
    img = Image.open(path)

    if flag == flag_list[0]:
        img = img.convert('RGB')
        img.save(os.path.join(new_path, new_name + '.jpg'), 'jpeg')
    elif flag == flag_list[1]:
        img = img.convert('RGB')
        img.save(os.path.join(new_path, new_name + '.jpeg'), 'jpeg')
    elif flag == flag_list[2]:
        img.save(os.path.join(new_path, new_name + '.png'), 'png')
    elif flag == flag_list[3]:
        img.save(os.path.join(new_path, new_name + '.gif'), 'gif')
    elif flag == flag_list[4]:
        img.save(os.path.join(new_path, new_name + '.bmp'), 'bmp')
    elif flag == flag_list[5]:
        img.save(os.path.join(new_path, new_name + '.tif'), 'tiff')


def img_resize(path, new_path, new_name, h, w):
    """
    重置文件大小（宽，高）
    :param path: 源图片路径
    :param new_path: 新图片保存路径 无图片名
    :param new_name: 新图片名称 含后缀
    :param h: 高
    :param w: 宽
    :return: None
    """
    img = Image.open(path)
    img.resize((h, w))
    img.save(os.path.join(new_path, new_name))


def img_clarity(img):
    """
    图片清晰度(仅供参考)
    :param img: 图片
    :return:
    """
    image = cv2.imread(img)
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    res = cv2.Laplacian(grayImg, cv2.CV_64F).var()
    return res


def create_qrcode(content, version=1, qrcode_name='qrcode.png'):
    """
    生成二维码
    :param content:
    :param qrcode_name:
    :return:
    """
    myqr.run(
        words=content,
        version=version,
        save_name=qrcode_name)


def decode_qrcode(qrcode_name):
    """
    获取二维码内容
    :param qrcode_name:
    :return:
    """
    img = Image.open(qrcode_name)
    qrcodes = pyzbar.decode(img)
    res = []
    for qrcode in qrcodes:
        data = qrcode.data.decode('utf-8')
        pos = qrcode.rect
        res.append([pos, data])
    return res


def cut(img, pos: tuple, res_img):
    Image.open(img).crop(pos).save(res_img)


# -----------------------------------
__all__ = [k for k, v in globals().items() if isinstance(v, types.FunctionType)]
