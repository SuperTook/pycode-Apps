from pyecharts.charts import Bar
from pyecharts import options as op
from pyecharts.globals import ThemeType as thm

# 设置行名
columns = ['夏朝', '商朝', '西周', '春秋', '战国', '秦朝', '西楚', '西汉', '新朝', '东汉', '三国',
           '西晋', '东晋', '南北朝', '隋朝', '唐朝', '五代', '十国', '宋朝', '元朝', '明朝', '清朝']
# 设置数据
coldata = [417, 438, 275, 294, 254, 16, 5, 210, 16, 199, 61,
           51, 103, 170, 38, 290, 54, 89, 320, 98, 277, 268]

(
    Bar(init_opts=op.InitOpts(theme=thm.LIGHT, width='1370px', height='550px'))
    .add_xaxis(columns)
    .add_yaxis("持续时间：", coldata)
    .render('render/各个朝代及持续的年份.html')
)