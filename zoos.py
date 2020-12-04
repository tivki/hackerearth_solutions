st=input()
x=0
y=0
for i in range(len(st)):
    if(st[i]=="z"):
        x+=1
    elif(st[i]=="o"):
        y+=1
if(y==(2*x)):
    print("Yes")
else:
    print("No")
