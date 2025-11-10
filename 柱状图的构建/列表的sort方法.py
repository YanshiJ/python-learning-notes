my_list = [["a",33],["b",12],["c",5]]
# 排序，基于带名函数
# def choose_sort_key(element):
#     return element[1]
# my_list.sort(key=choose_sort_key,reverse=True)
# print(my_list)
# 排序，基于lambda函数
my_list.sort(key = lambda element: element[1],reverse = True)
print(my_list)