#!usr/bin/env python
# _*_ coding:UTF-8 _*_
# 信息：
# 开发团队 ： C.zf
# 开发人员 ： C.Z.F
# 开发时间 ： 2020/7/10 19:59
# 文件名称 ： Office.py
# 开发工具 ： PyCharm
import os
import re
import codecs
import types
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileMerger

# For special variables of read/write (DOC_DEFAULT), the method:
#
# import conffey.Document as doc
# doc.DOC_DEFAULT = 'textFile.txt'
#
#
# write('My Title')   # write('My Title', file_path='textFile.txt')
# s = read()   # read('textFile.txt', ...)
#
# ss = input('In[1]:')
# write(ss)

DOC_DEFAULT = None


def create(file_name, file_path='./'):
    """
    新建文件
    :param file_name: 新文件名称(含后缀)
    :param file_path: 新文件路径
    :return: None
    """
    f = open(os.path.join(file_path, file_name), 'w+')
    f.close()


def delete(file_path, is_all=False):
    """
    删除文件
    :param file_path: 路径。如果is_all=False，则有路径有文件名(含后缀)。如果is_all=True，则只有路径无文件名。
    :param is_all: 是否删除目录下的全部文件
    :return: None
    """
    if not is_all:
        os.remove(file_path)
    elif is_all:
        for root, dirs, files in os.walk(file_path):
            for file in files:
                os.remove(os.path.join(root, file))


def read(file_path=DOC_DEFAULT, size=0, mode='r', coding='utf-8'):
    """
    读取文件
    :param file_path: 路径 包含文件名(含后缀)
    :param size: 读取多少个字符(从第一个到最后一个)。汉字、字母、数字、符号都按1个。如果要读取全部，则赋值0
    :param mode: 模式
    :param coding: 编码模式
    :return: <str> "文件内容"
    """
    if size != 0:
        with open(file_path, mode=mode, encoding=coding) as f:
            return f.read(size)
    else:
        with open(file_path, mode=mode, encoding=coding) as f:
            return f.read()


def write(*content, file_path=DOC_DEFAULT, mode='w', coding='utf-8', sep=''):
    """
    写入文件
    :param file_path: 文件路径 包含文件名(含后缀)
    :param content: 需要写入的内容
    :param mode: 模式
    :param coding: 编码模式
    :param sep: 分隔符
    :return: None
    """
    with open(file_path, mode=mode, encoding=coding) as f:
        if len(content) == 1:
            f.write(str(content[0]))
        else:
            for item in map(str, content):
                f.write(item + sep)


def rename(old, new):
    """
    重命名文件
    :param old: 原文件名(含路径)
    :param new: 新文件名(含路径)
    :return: <None>
    """
    if os.path.exists(old):
        os.renames(old, new)
    else:
        raise FileNotFoundError("File not found ({:s})".format(old))


def copy(source, target):
    """
    复制文件
    :param source: 源文件
    :param target: 新文件
    :return:
    """
    if not os.path.exists(source):
        raise FileNotFoundError("File not found ({:s})".format(source))

    with open(source, 'rb') as s:
        s_content = s.read()

    with open(target, 'wb') as t:
        t.write(s_content)


def shear(source, target):
    """
    剪切文件
    :param source: 原文件路径
    :param target: 新文件路径
    :return:
    """
    if not os.path.exists(source):
        raise FileNotFoundError("File not found ({:s})".format(source))

    with open(source, 'rb') as s:
        s_content = s.read()
    os.remove(source)

    with open(target, 'wb') as t:
        t.write(s_content)


def equals_extend(file_path='./', file_ext='all'):
    """
    遍历目录，并返回后缀名为需要的后缀名的文件的列表

    """
    file_list_rtn = []
    for root, dirs, files in os.walk(file_path):
        for one_file in files:
            file_dir = os.path.join(root, one_file)
            if file_ext == 'all':
                file_list_rtn.append(re.sub(r'\\', r'\\s', file_dir))
            elif os.path.splitext(file_dir)[1] == file_ext:
                file_list_rtn.append(re.sub(r'\\', '/', file_dir))
    file_list_rtn.sort()
    return file_list_rtn


def merging_pdf(path='./pdf', output_path='./merging.pdf', import_bookmarks=False):
    """
    合并 PDF
    :param path: 存放PDF的路径(如果有多个，则全部合并)
    :param output_path: 合并后的的PDF文件存放路径(含文件名)
    :param import_bookmarks: 是否导入书签
    :return: None
    """
    merger = PdfFileMerger()
    file_list = equals_extend(path, '.pdf')
    if len(file_list) == 0:
        raise FileNotFoundError('PDF files do not exist in this directory and its subdirectories')
    for file_name in file_list:
        f = codecs.open(file_name, 'rb')
        file_read = PdfFileReader(f)
        file_name_not_ext = os.path.basename(os.path.splitext(file_name)[0])

        if file_read.isEncrypted is True:
            print('\033[0;31mResourceWarning:\n\tUnsupported encrypted file "{:s}"\033[0m'.format(file_name))
            continue
        merger.append(file_read, bookmark=file_name_not_ext, import_bookmarks=import_bookmarks)
        f.close()
    merger.write(output_path)
    merger.close()


def pdf_page_num(path):
    """
    获取PDF总页数
    :param path: PDF路径
    :return: <int> 页码数
    """
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page_num = pdf.getNumPages()
    return page_num


def pdf_outline(pdf_path, list_path, is_page=True):
    """
    获取PDF大纲
    :param pdf_path: PDF路径
    :param list_path: 保存大纲的文件的路径
    :param is_page: 是否含页码
    :return: None
    """
    def get_outline(obj, __is_page):
        rtn = []
        for o in obj:
            if type(o).__name__ == 'Destination':
                if __is_page:
                    rtn.append(o.get('/Title') + '\t\t' + str(o.get('/Page') + 1) + '\n')
                else:
                    rtn.append(o.get('/Title') + '\n')
            elif type(o).__name__ == 'list':
                get_outline(o, __is_page)
        return rtn

    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        outlines = pdf.getOutlines()
        lst = get_outline(outlines, is_page)
        with open(list_path, 'w') as fl:
            for item in lst:
                fl.write(str(item))


def path_content(path):
    """
    获取目录下的目录和文件
    :param path: 路径
    :return: <tuple> ((路径下的目录), (路径下的文件), (文件数, 子目录数))
    """
    res_drs = []
    res_fls = []
    for root, dirs, files in os.walk(path):
        for dr in dirs:
            res_drs.append(re.sub(r'\\', '/', os.path.join(root, dr)))
        for fl in files:
            res_fls.append(re.sub(r'\\', '/', os.path.join(root, fl)))

    res = (tuple(res_drs), tuple(res_fls), (len(res_drs), len(res_fls)))
    return res


# -----------------------------------
__all__ = [k for k, v in globals().items() if isinstance(v, types.FunctionType)]
__all__.append('DOC_DEFAULT')
