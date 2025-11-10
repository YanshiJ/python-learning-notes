# if int(input('请输入你的身高：')) > 120:
#     print("sorry,you cant enter the zoo for free")
#     print("but,if your vip level bigger than 3,you can still play for free")
#     if int(input("please enter your vip level:")) > 3:
#         print("of course you can play for free")
#     else:
#         print("sorry,you cant enter the zoo for free")
# else:
#     print("you can play for free,have a nice day")

age = 25
year = 2
level = 5
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 3:
            print("恭喜你，你的入职时间足够了，可以获得礼品")
        elif level > 3:
            print("恭喜你，你的等级足够了，可以获得礼品")
        else:
            print("不好意思，无法领取礼品")
    else:
        print("不好意思，年龄太大了")
else:
    print("抱歉你还未成年")