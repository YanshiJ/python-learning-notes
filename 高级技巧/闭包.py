# 简单闭包
# def outer(logo):
#     def inner(msg):
#         print(logo,msg,logo)
#     return inner
# fn1 = outer("hello")    # 外部函数传入值无法被更改
# fn1("world")
# 使用nonlocal关键字修改外部函数的值
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#     return inner
# fn1 = outer(10)
# fn1(2)
# 使用闭包完成ATM小案例
def bank(initial_balance = 0):
    def operate(num,deposit = True):
        nonlocal initial_balance
        if deposit:
            initial_balance += num
            print(initial_balance)
        else:
            initial_balance -= num
            print(initial_balance)
    return operate
account = bank()
account(100)
account(100)
account(100)
account(100)