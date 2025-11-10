from data_define import record
from data_read import json_reader,file_reader,DataReader
from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='szgz89707515',
    autocommit=True
)
January = file_reader("F://2011年1月销售数据.txt")
February = json_reader("F://2011年2月销售数据JSON.txt")
jan_list: list[record] = January.read_data()
feb_list: list[record] = February.read_data()
# 将两个月份的数据合并为一个list
all_data = jan_list + feb_list
cursor = conn.cursor()
conn.select_db("py_sql")
for record in all_data:
    sql = (f"insert into orders(order_time,order_id,money,province) "
           f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')")
    cursor.execute(sql)
conn.close()

