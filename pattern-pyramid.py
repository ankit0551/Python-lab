row = eval(input())
for i in range(1,row+1):
    for k in range(1,row+1-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()