class Animal:
    def speak(self):
        pass        # 抽象方法
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def make_noise(animal:Animal):
    animal.speak()
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)
