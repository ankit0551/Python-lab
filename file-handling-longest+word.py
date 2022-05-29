with open('sample.txt','r') as f:
    temp = f.read().split()
    print(max(temp,key=len))