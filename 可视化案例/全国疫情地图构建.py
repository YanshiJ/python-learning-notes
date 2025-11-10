# 由于pyecharts版本新，无法实现与课程中一样的效果，但基本原理已经实现
from pyecharts.charts import Map
from pyecharts.options.global_options import VisualMapOpts, TitleOpts
import json
f = open("F://疫情.txt","r",encoding="utf-8")
data = f.read()
# 将json文件转换为python字典
data_dict = json.loads(data)
# 从字典中取出数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并将各个省数据都封装入列表中
data_list = []      # 绘图需要用到的list
for province_data in province_data_list:
    province_name = province_data["name"]# 省份名称
    province_name += "省"
    province_confirm = province_data["total"]["confirm"] # 确诊人数
    data_list.append((province_name,province_confirm))
print(data_list)
print(type(province_name))
map = Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    title_opts=TitleOpts(title = "全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,           # 是否显示
        is_piecewise=True,      # 是否分段
        pieces=[
            {"min": 1, "max": 99,"label":"1-99人","color":"#CCFFFF"},
            {"min": 100, "max": 999,"label":"100-999人","color":"#FFFF99"},
            {"min": 1000, "max": 4999,"label":"1000-4999人","color":"#FF9966"},
            {"min": 5000, "max": 9999,"label":"5000-9999人","color":"#FF6666"},
            {"min": 10000, "max": 99999,"label":"10000-99999人","color":"#CC3333"},
            {"min": 100000,"label":"100000以上","color":"#990033"},
        ]
    )
)
map.render()
f.close()