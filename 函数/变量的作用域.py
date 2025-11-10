# 局部变量
# def test_a():
#     num = 100
#     print(num)
# test_a()
# print(num)（变量只能在函数内部使用）
# 全局变量
# num = 200
# def test_a():
#     print(num)
# def test_b():
#     print(num)
# test_a()
# test_b()
# print(num)
# 在函数内修改全局变量
# num = 200
# def test_a():
#     print(num)
# def test_b():
#     num = 10
#     print(num)
# test_a()
# test_b()
# print(num)
# 利用global修改全局变量
num = 200
def test_a():
    print(num)
def test_b():
    global num
    num = 500
    print(num)
test_a()
test_b()
print(num)