import re
s = "1python hello python156488"
# 从开头开始匹配，没有就返回None
result = re.match("python",s)
print(result)
# print(result.span())
# print(result.group())
# search搜索匹配(依旧只找一个)
result = re.search("python",s)
print(result)
# findall搜索全部匹配
result = re.findall("python",s)
print(result)