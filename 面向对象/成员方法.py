# 1.定义一个带有成员方法的类
class student:
    name = None
    def say_hi(self):
        print(f"大家好，我是{self.name}，欢迎大家关照")
    def say_hello(self,msg):
        print(f"大家好，我是{self.name}，{msg}")
stu1 = student()
stu1.name = "james"
stu1.say_hi()
stu1.say_hello("hello")