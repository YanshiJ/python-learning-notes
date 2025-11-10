import time
# 打开文件
f = open("C:/Users/Yan/Desktop/test.txt","r",encoding="utf-8")
print(type(f))
# 读取文件 - read()
# print(f.read(10))# 读取十个字节
# print(f.read())# 读取全部字节（连续调用两次read，从上一次结束的地方往下继续）
# 读取文件 - readlines()
# lines = f.readlines() # 读取全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容：{lines}")
#读取文件  - 一次读取一行readline（）
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行{line1}")
# print(f"第二行{line2}")
# print(f"第三行{line3}")
# for循环读取文件行
for line in f:
    print(f"每一行的数据是：{line}")
# 文件的关闭
f.close()
time.sleep(500000)
# with open语法操作文件
with open("C:/Users/Yan/Desktop/test.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line) # 执行完成with open命令中的内容会自动关闭程序，不需要close
time.sleep(500000)