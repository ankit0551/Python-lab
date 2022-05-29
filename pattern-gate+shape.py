row=int(input())
for i in range(0,row):
    for j in range(0,row-i):
        print("*",end="")
    for k in range(2*i):
        print(" ",end="")
    for l in range(0,row-i):
        print("*",end="")
    print()