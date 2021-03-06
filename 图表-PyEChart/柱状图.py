from pyecharts.charts import Bar
from pyecharts import options as op
from pyecharts.globals import ThemeType as thm

# 设置行名
columns = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
# 设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

(
    Bar(init_opts=op.InitOpts(theme=thm.LIGHT))
    .add_xaxis(columns)
    .add_yaxis("降水量", data1)
    .add_yaxis("蒸发量", data2)
    .render('render/柱状.html')
)
