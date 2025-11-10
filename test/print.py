s = input("enter a string")
empty = ""
value = 3.14
if s.count(".")>1:
    print("invalid input")
else:
    for char in s:
        if char in "0123456789.":
            empty += char
        else:
            continue
    if empty != ""and empty != ".":
        empty = float(empty)
        result = empty + 3.14
        print(result)
    else:
        print("invalid input")
