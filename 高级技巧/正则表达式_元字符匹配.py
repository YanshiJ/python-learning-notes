import re

# s = "helovnfdjkvnk154981ca3cf1vbbdf3v1we5v864v5d12v"
# result = re.findall(r'\d',s)    # 字符串前面带上r标记，表示转义字符无效
# print(result)
# result = re.findall('[A-Za-z]',s)
# print(result)
# 匹配账号，只能由字母和数字组成，长度限制6-10位
# r = '^[0-9a-zA-Z]{6,10}$'
# s = '1232455'
# print(re.findall(r,s))
# 匹配qq号，要求纯数字，长度5-11，第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '12345678'
print(re.findall(r,s))
# 匹配邮箱地址，只允许qq,163,gmail
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'a.b.c.e.f.g.h@163.com.s.s.f.fe.e'
print(re.match(r,s))