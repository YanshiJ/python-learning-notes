class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # __str__魔术方法
    def __str__(self):
        return f"名字:{self.name}，年龄：{self.age}"
    # __lt__小于符号比较
    def __lt__(self,other):
        return self.age < other.age
    # __le__大于等于，小于等于比较
    def __le__(self,other):
        return self.age <= other.age
    # __eq__比较是否等于
    def __eq__(self,other):
        return self.age == other.age
stu1= student("james",19)
stu2 = student("hax",23)
print(stu1 == stu2)