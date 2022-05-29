st = {'name':'ravi','sec':'h','rolln':45}
a = 'h'
for i in st.copy():
    if st[i] == a:
        st.pop(i)
print(st)