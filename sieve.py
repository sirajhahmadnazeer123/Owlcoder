n=1000002
d=[1]*n
d[0]=0
d[1]=0
for i in range(2,int(n**0.5)+1):
    if d[i]==1:
        for j in range(i*i,n+1,i):
            d[j]=0
    
v=int(input())
for i in range(v):
    b=int(input())
    if d[b]:
        print(1)
    else:
        print(0)

    
