n = int(input("enter no of rows"))
for row in range(0,n):
    for col in range(0,row+1):
        print("*", end="")

    print("\r")