# def say_hi():
#     print("hi")
# result = say_hi()
# print(f"无返回值的函数，返回的内容是：{result}")
# print(f"无返回值的函数，返回的内容类型是：{type(result)}")
# 主动返回none的函数
def say_hello():
    print("hello")
    return None
result = say_hello()
print(f"无返回值的函数，返回的内容是：{result}")
print(f"无返回值的函数，返回的内容类型是：{type(result)}")
# none用于if判断
def check(age):
    if age > 18:
        return "success"
    else:
        return None
# if只能执行true语句。这里一旦接收到result为none，not none转成true输出if下面内容
result = check(16)
if not result:
    print("未成年，禁止进入")
