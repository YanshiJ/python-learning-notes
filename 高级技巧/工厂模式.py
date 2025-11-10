class Person:
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass
class Worker(Person):
    pass
class PersonFactory:
    def get_person(self,p_type):
        if p_type == 's':
            return Student
        elif p_type == 't':
            return Teacher
        else:
            return Worker

pf = PersonFactory()
student = pf.get_person('s')
teacher = pf.get_person('t')
worker = pf.get_person('w')