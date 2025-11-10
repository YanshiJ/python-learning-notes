# 基本捕获异常
# try:
#     f = open("D:/abc.txt","r",encoding="utf-8")
# except:
#     print("出现异常，因为文件不存在，将open模式改为w模式打开")
#     f = open("D:/abc.txt","w",encoding="utf-8" )
# 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print("出现了变量未定义的异常")
# 捕获多个异常
# try:
#     print(name)
#     # 1/0
# except (NameError,ZeroDivisionError) as e:
#     print("出现了变量未定义 或者 除以0的异常情况")
# 未正确设置捕获异常类型，将无法捕获异常
# 捕获所有异常，else，finally的用法
try:
    print(1)
except Exception as e:
    print("出现异常了")
else:
    print("恭喜没有异常")


try:
    f = open("D:/abc.txt","r",encoding="utf-8")
except:
    print("出现异常，因为文件不存在，将open模式改为w模式打开")
    f = open("D:/abc.txt","w",encoding="utf-8" )
finally:
    f.close()