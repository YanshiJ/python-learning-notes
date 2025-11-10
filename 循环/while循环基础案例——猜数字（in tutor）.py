import random
num = random.randint(1,10)
tried_times = 0
flag = True
while flag:
    answer = int(input("请输入你所猜测的数字:"))
    tried_times += 1
    if answer == num:
        print(f"恭喜你猜中了,总共花了{tried_times}次")
        flag = False
    else:
        if answer > num:
            print(f"猜大了哦，您已经尝试{tried_times}次")
        elif answer < num:
            print(f"猜小了哦，您已经尝试{tried_times}次")