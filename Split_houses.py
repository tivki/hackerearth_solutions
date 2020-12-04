-> The above code is for the split house problem of hackerearth.

n=int(input())

for i>=1 and i<=10:
    st=input()
    if "HH" in st:
        print("NO")
    else:
        st.replace(".","B")
        print("YES")
        print(st)
