import json
from data_define import record
# 基于两文件内容格式不同，先设计一个抽象类，确定有哪些需要实现的功能
class DataReader:
    def read_data(self) -> list[record]:
        """
        读取文件数据
        读到的每一条数据都转换为record对象
        将其都封装到list中并返回
        """
        pass
class file_reader(DataReader):
    def __init__(self, path):
        self.path = path
    def read_data(self) -> list[record]:
        f = open(self.path, 'r', encoding='utf-8')
        file_data = f.readlines()
        record_list = []
        f.close()
        for line in file_data:
            line = line.strip()   # 消除读取到的数据中的每一行的“\n”
            data_list = line.split(",")
            record_data = record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record_data)
        return record_list
class json_reader(DataReader):
    def __init__(self, path):
        self.path = path

    def read_data(self):
        f = open(self.path, 'r', encoding='utf-8')
        record_list = []
        for line in f.readlines():

            data_dict = json.loads(line)
            record_data = record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record_data)
        f.close()

        return record_list
if __name__ == '__main__':
    file1 = json_reader("F://2011年2月销售数据JSON.txt")
    list1 = file1.read_data()
    file2 = file_reader("F://2011年1月销售数据.txt")
    list2 = file2.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)