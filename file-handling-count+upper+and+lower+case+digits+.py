with open('sample.txt','r') as f:
    temp = f.read()
    
    v = 0
    d = 0
    alfa = 0
    w = 0
    for i in temp:
        if i.islower():
            v += 1
        elif i.isupper():
            alfa += 1
        elif '0' <= i <= '9':
            d += 1
        else:
            w += 1
    print(f"lower case: {v} \nupper case: {alfa} \ndigits: {d} \nspace: {w}")