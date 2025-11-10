# 构造方法的名称：__init__
class student:
    def __init__(self, name, age, tel): # 程序运行起来后自动运行
        self.name = name
        self.age = age
        self.tel = tel
stu1 = student("james", 20, "121564877")
print(stu1.name)
print(stu1.age)
print(stu1.tel)