my_dict = {"王力宏":99,"周杰伦":66,"严世锦":100}
# 新增元素
my_dict["张信哲"] = 66
print(my_dict)
# 更新元素
my_dict["周杰伦"] = 33
print(my_dict)
# 删除元素
score = my_dict.pop("周杰伦")
print(my_dict)
print(score)
# 清空元素
my_dict.clear()
print(my_dict)
# 获得字典中全部key
my_dict = {"王力宏":99,"周杰伦":66,"严世锦":100}
keys = my_dict.keys()
print(keys)
# 遍历字典
# 方式1
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value：{my_dict[key]}")
# 方式2
for key in my_dict:
    print(f"2字典的key是：{key}")
    print(f"2字典的value：{my_dict[key]}")
# 统计字典的元素数量
num = len(my_dict)
print(num)