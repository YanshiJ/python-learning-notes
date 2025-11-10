print("欢迎来到儿童游乐园，儿童免费，成人收费")
age = input("请输入你的年龄:")
age = int(age)
if age >= 18:
    print("你已经成年了")
    print("需要买票哦")
if age < 18:
    print("恭喜你，你还未成年哦")
print("祝您玩得愉快")