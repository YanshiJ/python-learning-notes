# 循环中断continue
# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")
# continue的嵌套使用
# for i in range(1,6):
#     print("语句1")
#     for j in range (1,6):
#         print("语句2")
#         continue
#         print("语句3")
# print("语句4")
# break语句的使用
# for i in range (1,101):
#     print("1")
#     break
#     print('2')
# print('3')
# break语句的嵌套使用
for i in range(1,11):
    print("1")
    for j in range (1,11):
        print("2")
        break
        print("3")
print("4")
