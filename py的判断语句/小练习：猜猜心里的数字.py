if int(input('请输入第一次猜想的数字：')) == 10:
    print("恭喜你猜对了")
elif int(input('不对哦，再试一遍：')) == 10:
    print("太棒啦，你猜对啦")
elif int(input("再试一遍吧~ ：")) == 10:
    print("终于对啦")
else:
    print("没猜出来哦，我想的是10！")