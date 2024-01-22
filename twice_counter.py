n=int(input())
d={}
l=list(map(str,input().split()))
c=0
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]==2:
        c+=1
print(c)
