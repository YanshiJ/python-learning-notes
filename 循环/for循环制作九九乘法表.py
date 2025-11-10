for i in range (1,10):
    print("")
    for j in range (1,10):
        if j <= i:
            print(f"\t{i}*{j}={i*j}",end = " ")
