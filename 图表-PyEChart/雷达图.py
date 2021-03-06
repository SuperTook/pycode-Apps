import pyecharts.options as opts
from pyecharts.charts import Radar
from pyecharts.globals import ThemeType as thm


v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

(
    Radar(init_opts=opts.InitOpts(width="1280px", height="640px"))
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="销售"),
            opts.RadarIndicatorItem(name="管理"),
            opts.RadarIndicatorItem(name="信息技术"),
            opts.RadarIndicatorItem(name="客服"),
            opts.RadarIndicatorItem(name="研发"),
            opts.RadarIndicatorItem(name="市场"),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="#fff"),
    )
    .add(
        series_name="预算分配",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
    )
    .add(
        series_name="实际开销",
        data=v2,
        linestyle_opts=opts.LineStyleOpts(color="#5CACFF"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="雷达图"), legend_opts=opts.LegendOpts()
    )
    .render("render/雷达.html")
)