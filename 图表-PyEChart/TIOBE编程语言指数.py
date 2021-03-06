import pyecharts.options as opts
from pyecharts.charts import Pie
from requests import get
from bs4 import BeautifulSoup
from re import sub


response = get('https://www.tiobe.com/tiobe-index/')
table = '<thead>' + ''.join([str(t) for t in BeautifulSoup(response.text, 'lxml').find('table').contents])
tbody = '<tbody>' + ''.join([str(t) for t in BeautifulSoup(table, 'lxml').find('tbody').contents])
tr = BeautifulSoup(tbody, 'lxml').find_all('tr')
td = [r.contents for r in tr]
name = [sub(r'<td>|</td>', '', str(d[3])) for d in td]
indx = [float(sub(r'<td>|</td>', '', str(d[4])).strip('%')) for d in td]

(
    Pie(init_opts=opts.InitOpts())
    .add('TIOBE编程语言指数', [(a, b) for a, b in zip(name, indx)], label_opts=opts.LabelOpts())
    .render('render/TIOBE编程语言指数.html')
)
