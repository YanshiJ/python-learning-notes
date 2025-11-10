N = int(input('N: '))
for i in range(1, N + 1):
    for k in range(1, N + 1):
        if (i + k) % 2 == 0:
            print("#", end="")
        else:
            print(".", end = "")
    print()



