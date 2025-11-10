import time
# 打开文件，不存在的文件
# f = open("D:/test.txt","w",encoding = "utf-8")
# # write写入
# f.write("hello world")
# # flush刷新
# f.flush()
# # 关闭文件
# f.close()           # close方法自带flush功能
# # 打开一个存在的文件
f = open("D:/test.txt","w",encoding = "utf-8")
f.write("niubi")
f.close()