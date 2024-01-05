n=list(map(str,input().split()))
k=[]
c=0
for i in n:
    if i.count("1")!=0:
        k.append(i.count("1"))
for  i in range(0,len(k)-1):
    c+=k[i]*k[i+1]
print(c)
    

