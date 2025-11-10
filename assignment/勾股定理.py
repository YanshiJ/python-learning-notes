print("WELCOME using Pythagorean equation calculator")
print("please enter the sides you know")
print("enter nothing if you don't know")
a = input("a = ")
b = input("b = ")
c = input("c = ")
if a is not None and b is not None and c == "":
    a= float(a)
    b= float(b)
    c = (a**2 + b**2)**0.5
    print(f"c = {c:.2f}")
if a == "" and b is not None and c is not None:
    b = float(b)
    c = float(c)
    if c <= b:
        print("Invalid input")
    else:
        a = (c**2-b**2)**0.5
        if c <= a:
            print("Invalid input")
        else:
            print(f"a = {a:.2f}")
if a is not None and b == "" and c is not None:
    a = float(a)
    c = float(c)
    if c <= a:
        print("Invalid input")
    else:
        b = (c ** 2 - a ** 2) ** 0.5
        if c <= b:
            print("Invalid input")
        else:
            print(f"b = {b:.2f}")