import random
num = random.randint(1,10)
guess_num = int(input("输入你所猜测的数字"))
if num == guess_num:
    print("恭喜，你第一次就猜中了")
else:
    if num > guess_num:
        print("猜小了哦")
    elif num < guess_num:
        print("猜大了哦")
    guess_num = int(input("再次输入你所猜测的数字"))
    if num == guess_num:
        print("恭喜你猜中了，花了两次机会")
    else:
        if num > guess_num:
            print("猜小了哦")
        elif num < guess_num:
            print("猜大了哦")
        guess_num = int(input("第三次输入你所猜测的数字"))
        if num == guess_num:
            print("恭喜你猜中了，花了三次机会")
        else:
            print("游戏失败啦，再来一次？")
