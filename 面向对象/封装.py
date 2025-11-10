# 定义一个类，内含有私有成员变量和私有成员方法
class phone:
    __current_voltage = 0.5 # 当前手机的运行电压
    def __keep_single_core(self):
        print("让CPU以单核模式运行")
    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行省电")
phone1 = phone()
# phone1.__keep_single_core()
# print(phone1.__current_voltage)
# 都是报错，因为是私有的
phone1.call_by_5G()