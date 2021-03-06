from pyecharts.charts import Pie
from pyecharts import options as op
from pyecharts.globals import ThemeType as thm

# 设置行名
columns = ["Python", "C", "Java", "JavaScript", "C++", "C#", "Visual Basic", "SQL", "PHP", "R"]
# 设置数据
data = [11.28, 16.95, 12.56, 2.14, 6.94, 4.16, 3.97, 1.57, 2.09, 1.99]

(
    Pie(init_opts=op.InitOpts(theme=thm.LIGHT))
    .add('TIOBE', [(a, b) for a, b in zip(columns, data)])
    .render('render/饼状.html')
)
