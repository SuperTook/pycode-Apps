from pyecharts.charts import Liquid
from pyecharts import options as opts
from pyecharts.globals import ThemeType as thm

(
    Liquid(init_opts=opts.InitOpts(width="600px", height="600px", theme=thm.LIGHT))
    .add(series_name="业务指标", data=[[0.98, '完成度']], shape='circle')
    # sharp水球外形，
    # 有' circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow' 可选
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{c} : {b}%"),
    )
    .render("render/水球.html")
)
