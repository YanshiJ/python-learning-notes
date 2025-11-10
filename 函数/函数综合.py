money = 5000000
x = 0
name = input("请输入您的姓名：")
def main():
    print("----------主菜单----------")
    print(f"您好{name}，欢迎来到本银行ATM，请选择操作：")
    print("查询存款\t【输入1】\n存款\t\t【输入2】\n取款\t\t【输入3】\n退出\t\t【输入4】")

def money_check():
    print("----------余额查询----------")
    print(f"{name}，您好，您的余额剩余：{money}")
def putin_money(x):
    x = int(input("请输入您存钱的金额："))
    global money
    money += x
    print("----------存款----------")
    print(f"{name}，您存款{x}成功")
    print(f"{name}，您好，您的余额剩余{money}")
    return money
def takeout_money(x):
    x = int(input("请输入您取钱的金额："))
    global money
    money -= x
    print("----------取款----------")
    print(f"{name}，您取款{x}成功")
    print(f"{name}，您好，您的余额剩余{money}")
    return money
main()
for press in range (1,5):
    press = input()
    if press == "1":
        money_check()
        main()
    elif press == "2":
        putin_money(x)
        main()
    elif press == "3":
        takeout_money(x)
        main()
    elif press == "4":
        print("您已退出，感谢您的光临")
        break