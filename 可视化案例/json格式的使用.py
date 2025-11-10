import json
data = [{"name":"jane","age":17},{"name":"jack","age":15},{"name":"jason","age":"18"}]
# 准备列表，将列表格式转换为json
json_str = json.dumps(data)
print(json_str)
print(type(json_str))
# 准备字典，将字典转换为json
data2 = {"name":"jane","age":17}
json_str2 = json.dumps(data2)
print(json_str2)
print(type(json_str2))
# 将json转换为python文件格式
s = '[{"name":"jane","age":17},{"name":"jack","age":15},{"name":"jason","age":"18"}]'
print(type(s))
l = json.loads(s)
print(l)
print(type(l))