height = int(input('请输入你的身高：'))
vip_level = int(input('请输入你的vip等级：'))
day = int(input('请输入今天的日期：'))
if height < 120:
    print("身高过关，可以免费游玩")
elif vip_level > 3:
    print("等级过关，可以免费游玩")
elif day == 1:
    print("今天是1号，可以免费游玩")
else:
    print("抱歉您不满足免费游玩条件")
    print("请前往购票处购票")
print("祝您游玩愉快")
# input可以放在if中使代码简洁