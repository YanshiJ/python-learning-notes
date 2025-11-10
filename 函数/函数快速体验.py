# 需求，统计字符串的长度，且不适用内置函数len()

str1 = "ysj"
str2 = "love"
str3 = "lzn"
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")

# 使用函数简化过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是：{count}")


my_len(str1)
my_len(str2)
my_len(str3)