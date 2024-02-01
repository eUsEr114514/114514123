from pyecharts.charts import Line

line = Line()
line.add_xaxis(["抖音", "bilibili", "全平台"])
line.add_yaxis("粉丝数", [12062, 20593, 45000])
line.render()


