name = "ysj"
message = "hello %s" % name
print(message)

age = 17
message = "hello my name is %s and my age is %s" % (name,age)
print(message)

"""
py中有三种占位形式
%s 是字符串（string）
%d 是整数（int）
%f 是浮点数（float）
"""
height = 175.2
message = "hello my name is %s and my age is %d,my height is %.1f" % (name,age,height)
print(message)

num1 = 11
num2 = 11.345
print("数字11的宽度限制为5，结果是%5d" % num1)
print("数字11的宽度限制为1，结果是%1d" % num1)
print("数字11的宽度限制为1，结果是%.11d" % num1)
print("数字11.345的宽度限制为5，小数精度2，结果是%7.2f" % num2)
print("数字11.345的宽度不限制，小数精度4，结果是%.4f" % num2)