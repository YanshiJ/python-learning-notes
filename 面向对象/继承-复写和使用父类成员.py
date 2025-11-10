class Phone:
    IMEI = None
    producer = "Apple"
    def call_by_4g(self):
        print("使用4g通话")
# 定义子类，复写父类
class newPhone(Phone):
    IMEI = None
    producer = "Huawei"
    def call_by_4g(self):
        print("更新过的4g通话")
        # 方式1
        # print(f"父类的厂商是{Phone.producer}")
        # Phone.call_by_4g()
        # 方法2
        print(f"父类的厂商是{super().producer}")
        super().call_by_4g()
iphone = newPhone()
print(iphone.producer)
iphone.call_by_4g()
