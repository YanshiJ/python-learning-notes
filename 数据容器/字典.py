# 定义字典(键值对)
my_dict = {"王力宏":99,"周杰伦":66,"严世锦":100}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(my_dict)
print(my_dict2)
print(my_dict3)
print(type(my_dict))
print(type(my_dict2))
print(type(my_dict3))
# key不允许重复
# 不可以使用下标索引
# 从字典中获取基于key的value
score = my_dict["王力宏"]
print(score)
# 定义嵌套字典
stu_score_dict = {"王力宏":{
    "chinese":77,
    "math":66,
    "english":100
},"周杰伦":{
    "chinese":55,
    "math":99,
    "english":35
},"严世锦":{
    "chinese":99,
    "math":99,
    "english":99
}}
# 从嵌套字典获取数据
print(stu_score_dict["严世锦"]["chinese"])