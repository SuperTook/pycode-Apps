# _*_ coding:utf-8 _*_
from conffey.Console import __all__ as __con_all
from conffey.Document import __all__ as __doc_all
from conffey.Picture import __all__ as __pic_all
from conffey.Console import *
from conffey.Document import *
from conffey.Picture import *


__version__ = '5.0.0'

t = []
for i in __con_all:
    t.append(i)
for i in __doc_all:
    t.append(i)
for i in __pic_all:
    t.append(i)

__all__ = t
__all__.append('__version__')
