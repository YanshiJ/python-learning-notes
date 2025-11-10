temp = float(input("请输入您的体温"))
def check():

    if temp > 37.2:
        print(f"欢迎来到此处，请出示您的健康码，"
              f"您的体温是{temp}，体温过高不可进入")
    else:
        print(f"欢迎来到此处，请出示您的健康码，"
              f"您的体温是{temp}，体温正常可以进入")
check()