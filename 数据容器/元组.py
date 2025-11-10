# 定义元组（元组和list的区别是元组中的元素不可以被修改）
t1 = (1,"hello",True)
t2 = ()# 空
t3 = tuple()# 空
print(f"t1的类型是：{type(t1)}，内容是：{t1}")
print(f"t2的类型是：{type(t2)}，内容是：{t2}")
print(f"t3的类型是：{type(t3)}，内容是：{t3}")
# 定义单个元素的元组
t4 = ("hello", )
print(f"t4的类型是{type(t4)},t4的内容是{t4}")
# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是{type(t5)},t4的内容是{t5}")
# 下标索引取出内容
print(t5[1][2])
# 元组的操作：index查找方法
t6 = ("mary","jane","jim")
index = t6.index("jim")
print(index)
# 元组的操作：count统计方法
t7 = ("mary","jane","jim","jim","jim","jim","jim","jim")
count = t7.count("jim")
print(count)
# len函数统计元组元素数量
t8 = ("mary","jane","jim","jim","jim","jim","jim","jim")
length = len(t8)
print(length)
# 元组的遍历：while循环
index = 0
while index < length:
    print(f"元组的元素有：{t8[index]}")
    index += 1
#元组的for循环遍历
for i in t8:
    print(i)