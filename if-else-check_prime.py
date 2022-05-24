num=eval(input("Enter the number" ))
flag=0
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        flag=1
        break;

if(flag==0):
    print("prime")