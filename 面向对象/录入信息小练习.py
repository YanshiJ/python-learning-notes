class info:
    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add
for student in range(1,11):
    print(f"当前输入第{student}位学生信息，总共需要录入10位学生")
    student_info = info(name = input("请输入学生姓名："),age = input("请输入学生年龄："),add = input("请输入学生住址："))
    print(f"学生{student}信息录入成功，信息为【学生姓名：{student_info.name}，年龄：{student_info.age}，住址：{student_info.add}】")