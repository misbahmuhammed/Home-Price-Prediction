input1=int(input("enter no of mountains"))
input2=int(input("enter the height of mountains range of A"))
input3=int(input({"enter the height of mountains range of B"}))
count = 0
for i in range(1,input1-1,i=i+1):
    if input2[i]!= input3[i]:
        input2[i]=input[2]-1
        input2[i+1]=input[i+1]-1
        count=count+1
b=0
for i in range(1,input1,i+1):
    if input2[i]==input3[i] and input2[i]>0:
        b=1
    else:
        break
if b==1:
    print(count)
else:
    print(-1)

        
