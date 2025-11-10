# 单继承
class Phone:
    IMEI = None
    producer = "Apple"
    def call_by_4g(self):
        print("使用4g通话")

class Phone2022(Phone):
    face_id = "100001"
    def call_by_5g(self):
        print("2022年新功能，使用5g通话")
Iphone = Phone2022()
Iphone.call_by_4g()
print(Iphone.producer)
# 多继承
class Phone:
    IMEI = None
    producer = "Apple"
    def call_by_4g(self):
        print("使用4g通话")
class NFCreader:
    nfc_type = "第五代"
    producer = "huawei"


    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class remote_controller:
    rc_typer = ("红外遥控")
    def control(self):
        print("红外遥控开启了")
class xiaomi_phone(Phone, NFCreader, remote_controller):
    pass
phone = xiaomi_phone()
phone.control()
phone.write_card()
phone.call_by_4g()
print(phone.rc_typer)
# 同名的属性被输入时，左边的优先