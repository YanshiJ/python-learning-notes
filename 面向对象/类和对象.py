# 设计一个闹钟类
class clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)
# 构建两个闹钟并让其工作
clock_1 = clock()
clock_1.id = "003202"
clock_1.ring()
print(clock_1.id)
clock_2 = clock()
clock_2.id = "003203"
clock_2.ring()
print(clock_2.id)