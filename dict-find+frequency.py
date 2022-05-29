st = input("enter the string ")
dct = {}
for i in st:
    if i not in dct:
        dct[i] = st.count(i)
for i,j in dct.items():
    print(i,j,sep=" : ")