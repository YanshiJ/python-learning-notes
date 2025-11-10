# 字符串是不可被修改的数据容器
name = "hello world"
# 通过下表索引取值
value = name[2]
print(value)
value = name[-10]
print(value)
# index方法(寻找起始下标)
index = name.index("world")
print(index)
# replace方法
new_name = name.replace("hello","my")
print(f"将字符串{name}替换后得到{new_name}")
# split分割
name = "it is good to see you"
name_split = name.split(" ")
print(name_split)
# strip方法(生成新的字符串，默认删去前后空格)
name = "       it is good to see you        "
new_name = name.strip()
print(new_name)
name = "12it is good to see you21"
new_name = name.strip("12")
print(new_name)
# 统计字符串中某字符串出现的次数
name = "hello hello ,nice to meet you"
num = name.count("hello")
print(num)
# 统计字符串的长度（空格算一个）
name = "hello "
length = len(name)
print(length)