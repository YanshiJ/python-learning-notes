def list_while_func():
    mylist = ["mary","jane","jack"]
    index = 0
    while index < len(mylist):
        print(mylist[index])
        index += 1
        if index == len(mylist):
            break
def list_for_func():
    mylist = ["mary","jane","jack"]
    for i in mylist:
        print(i)
list_while_func()
list_for_func()