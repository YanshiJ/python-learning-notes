# 定义集合(去重)(集合无序，不支持下表索引访问)
my_set = {"hello","world","nice","hello","world","nice","hello","world","nice"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")
# 追加新元素（允许修改）
my_set.add("PYTHON")
print(my_set)
# 移除元素
my_set.remove("hello")
print(my_set)
# 随机取出一个元素
my_set = {"hello","world","nice","hello","world","nice","hello","world","nice"}
takeout = my_set.pop()
print(takeout)
print(my_set)
# 清空集合
my_set.clear()
print(f"集合被清空，剩下{my_set}")
# 取两个集合的差集(在下方例子中代表集合1有的集合2没有的)
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(set3)
print(set1)
print(set2)
# 消除两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(set1)
print(set2)
# 两个集合的合并
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(set3)
print(set1)
print(set2)
# 统计集合元素数量
set1 = {1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5}
length = len(set1)
print(length)
# 集合的遍历
# 集合不支持下表索引，不支持while循环
# 但是可以使用for循环
set1 = {1,2,3,4,5}
for element in set1:
    print(element)

