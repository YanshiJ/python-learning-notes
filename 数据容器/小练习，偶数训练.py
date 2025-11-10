even_num_list = [ ]
num_list = [1,2,3,4,5,6,7,8,9,10]
def while_func():
    index = 0
    while index < len(num_list):
        if num_list[index] % 2 == 0:
            even_num_list.append(num_list[index])
        index = index + 1
    print(num_list)
    print(even_num_list)

def for_func():
    for num in num_list:
        if num % 2 == 0:
            even_num_list.append(num)
    print(num_list)
    print(even_num_list)

while_func()