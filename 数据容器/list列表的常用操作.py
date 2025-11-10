mylist = ["mary","john","jim"]
# 查找某元素在列表内的下标索引
index = mylist.index("jim")
print(f"jim在列表中的下标索引值是：{index}")
# 若所想要查找的元素不存在，会报错
# index = mylist.index("hello")
# print(f"hello在列表中的下标索引值是：{index}")
# 修改特定下表索引的值
mylist[0] = "ysj"
print(f"列表被修改后所打出的列表元素是{mylist}")
# 在指定下标处插入新元素
mylist.insert(1,"best")
print(f"添加后列表中的元素有{mylist}")
# 元素的追加（到尾部）（单个）
mylist.append("nb")
print(f"追加后列表中的元素有{mylist}")
# 追加一批元素
mylist2 = [[1,2,3],[3,4,5]]
mylist.extend(mylist2)
print(f"追加完一批元素后变成{mylist}")
# 删除元素（两种方法）
# 方法1
mylist = ["mary","john","jim"]
del mylist[0]
print(f"列表删除元素后{mylist}")
# 方法2
mylist = ["mary","john","jim"]
element = mylist.pop(2)
print(f"通过pop删除元素后的列表为{mylist}，被删除的元素是{element}")
# 删除某元素在列表中的第一个匹配量
mylist = ["mary","john","jim","jim","mary"]
mylist.remove("jim")
print(f"删除某元素在列表中的第一个匹配量后的列表为{mylist}")
# 清空列表
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")
# 统计某元素在列表中的数量
mylist = [1,2,3,2,5,4,5,3,2,1,3,2,1,2,1,21,1,1,1,1,1,1]
mylist.count(1)
print(f"这个列表中，有{mylist.count(1)}个")
# 统计列表中全部的元素数量
mylist = [1,2,3,2,5,4,5,3,2,1,3,2,1,2,1,21,1,1,1,1,1,1]
count = len(mylist)
print(f"列表总共有{count}个元素")