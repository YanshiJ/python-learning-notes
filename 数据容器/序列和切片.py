# 对list进行切片，从1开始，4结束（不包含第四位），步长1
my_list = [0,1,2,3,4,5,6,7,8,9]
result1 = my_list[1:4]       # 步长默认是1，可以省略不写
print(f"结果1：{result1}")
# 对tuple进行切片，从头开始，最后结束，步长1
my_tuple = (1,2,3,4,5,6,7,8,9)
result2 = my_tuple[ : ]
print(result2)        # 起始和结束不写表示从头到尾，步长为1可以省略
# 对str进行切片，从头到尾，步长2
my_str = "123456789"
result3 = my_str[::2]
print(result3)
# 对str反向切片
my_str = "123456789"        #等同于将序列反转
result4 = my_str[::-1]
print(result4)
# 对列表进行切片，从3开始，到1结束，步长-1(倒序时反过来)
my_list = [0,1,2,3,4,5,6,7,8,9]
result5 = my_list[3:1:-1]
print(result5)
# 对元组进行切片，从头到尾，步长-2
my_tuple = (1,2,3,4,5,6,7,8,9)
result6 = my_tuple[ : :-2]
print(result6)