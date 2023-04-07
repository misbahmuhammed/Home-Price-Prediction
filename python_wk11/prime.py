num = int(input("enter the number"))
flag = False

if num==1:
    print("its not a prime num")
elif num >1:
    for i in range(2,num):
            if(num%i)==0:
                flag =True
                break
    if flag:
         print("its not a prime")
    else:
        print("its a prime")
