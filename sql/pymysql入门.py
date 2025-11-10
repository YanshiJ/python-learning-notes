from pymysql import Connection
# 构建到mysql数据库的链接
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='szgz89707515',
)
# print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()     # 获取游标对象
# 选择数据库
conn.select_db('world')
# 执行sql
# cursor.execute("create table test_pymysql(id int);")
cursor.execute('select * from student')
results = cursor.fetchall() # type:tuple
print(results)
for r in results:
    print(r)


conn.close()