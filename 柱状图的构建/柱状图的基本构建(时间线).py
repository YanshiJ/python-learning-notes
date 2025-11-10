from pyecharts.charts import Bar , Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType
# 使用Bar构建基础柱状图
bar1 = Bar()
# 添加x轴数据
bar1.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar1.add_yaxis("GDP",[30,30,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()


# 使用Bar构建基础柱状图
bar2 = Bar()
# 添加x轴数据
bar2.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar2.add_yaxis("GDP",[50,50,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
# 使用Bar构建基础柱状图
bar3 = Bar()
# 添加x轴数据
bar3.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
bar3.add_yaxis("GDP",[70,60,30],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
timeline = Timeline({"theme": ThemeType.LIGHT})
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
# 设置自动播放
timeline.add_schema(
    is_timeline_show=True, # 是否显示时间线
    is_auto_play=True, # 是否自动播放
    is_loop_play=True, # 是否循环播放
    play_interval=1000 # 自动播放时间间隔
)



timeline.render("基础时间线柱状图.html")