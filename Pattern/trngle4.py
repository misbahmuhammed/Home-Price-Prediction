n=int(input("enter rows"))
for row in range(n):
    for col in range(row+1):
        print("_",end="")
    for col in range(row,n):
        print("*",end="")
    print()
