from pyecharts.charts import Funnel
from pyecharts import options as opts
from pyecharts.globals import ThemeType as thm


# 设置行名
columns = ["Python", "C", "Java", "JavaScript", "C++", "C#", "Visual Basic", "SQL", "PHP", "R"]
# 设置数据
data = [11.28, 16.95, 12.56, 2.14, 6.94, 4.16, 3.97, 1.57, 2.09, 1.99]

(
    Funnel(opts.InitOpts(width='900px', height='600px', theme=thm.LIGHT))
    .add('TIOBE编程语言指数', [(a, b) for a, b in zip(columns, data)])
    .render('render/漏斗.html')
)