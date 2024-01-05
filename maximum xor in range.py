a,b=map(int,input().split())
mx=0
for i in range(a,b+1):
    for j in range(a,b+1):
        cur=i^j
        mx=max(cur,mx)
print(mx)
#1<=a<b<=10000
