# 1.设计一个类（类比生活中：设计一张登记表）
class student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None
# 2.创建一个对象（类比生活中：打印一张登记表）
stu_1 = student()
stu_2 = student()
# 3.对象属性进行赋值（类比生活中：填写表单）
stu_1.name = "james"
stu_1.gender = "M"
stu_1.nationality = "US"
stu_1.native_place = "London"
stu_1.age = 28
# 4.获取对象中记录的信息
print(stu_1.age)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.gender)
print(stu_1.name)