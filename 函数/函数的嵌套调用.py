# 定义func_b
def func_b():
    print("---2---")
# 定义func_a
def func_a():
    print("---1---")
    func_b()
    print("---3---")
func_a()