nrow = int(input("number of rows: "))
ncol = int(input("number of columns: "))
# cols can be used as a sequence of letters A, B, C, ...
cols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:ncol]
for i in range(1,nrow+1):
    for j in range(ncol):
        print(cols[j]+str(i), end=" ")
    print()



