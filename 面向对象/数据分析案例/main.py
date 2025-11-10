from data_define import record
from data_read import json_reader,file_reader,DataReader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


January = file_reader("F://2011年1月销售数据.txt")
February = json_reader("F://2011年2月销售数据JSON.txt")
jan_list: list[record] = January.read_data()
feb_list: list[record] = February.read_data()
# 将两个月份的数据合并为一个list
all_data = jan_list + feb_list
# 开始进行数据计算
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        # 当前日期已经有记录了
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
print(data_dict)

# 可视化图表开发
bar = Bar(init_opts= InitOpts(theme = ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(
        title = "每日销售额"
    )
)
bar.render("销售额统计.html")