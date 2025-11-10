from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='szgz89707515',
    autocommit=True     # 自动提交
)
cursor = conn.cursor()
conn.select_db('test')
cursor.execute("insert into test_pymsql2 values (1,'james',16)")
# 通过commit进行确认
# conn.commit()
conn.close()