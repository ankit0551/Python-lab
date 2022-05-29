with open('sample.txt','r') as f:
    temp = f.read().split()
    le = max(temp,key=len)
    re = []
    for i in temp:
        if len(i) == len(le):
            re.append(i)
    print(re)
