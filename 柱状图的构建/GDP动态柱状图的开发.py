from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts, TitleOpts
from pyecharts.globals import ChartType, ThemeType

f = open("F://1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()
f.close()
data_lines.pop(0)
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0]) # 拿到年份
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 如何判断字典里面有没有指定的key
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])
timeline =  Timeline({"theme":ThemeType.LIGHT})
# 排序年份
sorted_years = sorted(data_dict.keys())
for year in sorted_years:
    data_dict[year].sort(key = lambda element: element[1],reverse = True)
    # 取出本年份前八名
    year_data = data_dict[year][0:7]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    # 设置每一年图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title = f"{year}年全球前八GDP")
    )
    timeline.add(bar,str(year))
timeline.add_schema(
    is_timeline_show=True,
    is_loop_play=True,
    is_auto_play=True,
    play_interval=1000
)
timeline.render("GDP动态图.html")