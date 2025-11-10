from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
import json
f_us = open("F://美国.txt","r",encoding="utf-8")
f_jp = open("F://日本.txt","r",encoding="utf-8")
f_id = open("F://印度.txt","r",encoding="utf-8")
us_data = f_us.read()
jp_data = f_jp.read()
id_data = f_id.read()
# usdata目前是str文件，是f_us通过read方法得出的
# 删除开头不符合规范的字符
us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
id_data = id_data.replace("jsonp_1629350745930_63180(","")
# 删除结尾不符合规范的字符
us_data = us_data[:-2]
jp_data = jp_data[:-2]
id_data = id_data[:-2]
# json转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
id_dict = json.loads(id_data)
# 获得trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
id_trend_data = id_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年（到315下标结束）
us_x_data = us_trend_data['updateDate'][:314:1]
jp_x_data = jp_trend_data['updateDate'][:314:1]
id_x_data = id_trend_data['updateDate'][:314:1]
# 获取确诊数据
us_y_data = us_trend_data['list'][0]['data'][:314:1]
jp_y_data = jp_trend_data['list'][0]['data'][:314:1]
id_y_data = id_trend_data['list'][0]['data'][:314:1]
# 生成图表
line = Line()
# 添加x轴
line.add_xaxis(us_x_data)
# 添加y轴
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",id_y_data,label_opts=LabelOpts(is_show=False))
# 润色修改，标题等(全局选项)
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title = "2020年美日印三国确诊人数折线图",pos_left="center",pos_bottom="1%"),
)
# 调用render方法生成图表
line.render()
# 关闭文件
f_us.close()
f_jp.close()
f_id.close()