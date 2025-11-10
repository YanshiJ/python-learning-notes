from pyecharts.charts import Map
import json
from pyecharts.options.global_options import TitleOpts, VisualMapOpts
f = open("F://疫情.txt","r",encoding="utf-8")
data = f.read()
data_dict = json.loads(data)
henan_data = data_dict["areaTree"][0]["children"][3]
henan_city_data = henan_data["children"]
henan_data_list = []
for city in henan_city_data:
    city_name = city["name"]
    city_confirm = city["total"]["confirm"]
    city_name += "市"
    henan_data_list.append((city_name,city_confirm))
henan_data_list.append(("济源市",5))
print(henan_data_list)
f.close()
map = Map()
map.add("各个市的确诊人数",henan_data_list,"河南")
map.set_global_opts(
    title_opts=TitleOpts(title = "河南省疫情分布情况"),
    visualmap_opts=VisualMapOpts(
        is_show = True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99,"label":"1-99人","color":"#CCFFFF"},
            {"min": 100, "max": 999,"label":"100-999人","color":"#FFFF99"},
            {"min": 1000, "max": 4999,"label":"1000-4999人","color":"#FF9966"},
            {"min": 5000, "max": 9999,"label":"5000-9999人","color":"#FF6666"},
            {"min": 10000, "max": 99999,"label":"10000-99999人","color":"#CC3333"},
            {"min": 100000,"label":"100000以上","color":"#990033"},]

    )

)
map.render("河南省疫情地图.html")
