import random
num = random.randint(1,10)
answer = int(input("让我们一起来猜数字吧："))
tried_times = 0
while answer != num:
    if answer > num:
        tried_times += 1
        print(f"您已尝试{tried_times}次")
        answer = int(input("猜大了哦，再试试吧"))
    elif answer < num:
        tried_times += 1
        print(f"您已尝试{tried_times}次")
        answer = int(input("猜小了哦，再试试看"))
else:
    tried_times += 1
    print(f"恭喜你猜对啦,总共用了{tried_times}次哦")