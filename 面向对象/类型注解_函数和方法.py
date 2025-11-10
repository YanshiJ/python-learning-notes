# 对形参进行类型注解
def add(x:int, y:int):
    return x + y
# 对返回值进行注解
def func2(data:list) -> list:
    return data
print(func2([1,2,3]))