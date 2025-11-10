# 定义一个函数
# 接收另一个函数作为传入参数
def test_func(add):
    result = add(1,2)
    print(type(add))
    print(result)
def add(a,b):
    return a+b
test_func(add)
# 传入计算逻辑，而非传入数据