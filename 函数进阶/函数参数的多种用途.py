def user_info(name,age,gender):
    print(f"您的姓名是{name}，年龄是{age}，性别是：{gender}")
# 位置传参
user_info("严世锦",17,"male")
# 关键字传参
user_info(name="严世锦",age=17,gender="male")
user_info(age=17,name="严世锦",gender="male")# 可以不按顺序
user_info("严世锦",gender="male",age=17)# 混合使用
# 缺省参数（给予默认值）
def user_info(name,age,gender="male"):
    print(f"您的姓名是{name}，年龄是{age}，性别是：{gender}")
user_info("严世锦",17)
user_info("赖梓楠",age = 18,gender = "female")
# 不定长 - 位置不定长，*号
# 不定长定义的形式参数会作为元组存在，接受不定长数量的参数传入
def user_info(*args):
    print(f"*args参数的类型是：{type(args)}，内容是{args}")
user_info(1,"hello",True)
# 不定长 - 关键字不定长**号
def user_info(**kwargs):
    print(f"*args参数的类型是：{type(kwargs)}，内容是{kwargs}")
user_info(name = "hello",age = 17,gender = "female")