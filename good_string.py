# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    f=input()
    mx=0
    c=1
    for i in range(0,len(f)-1):
        if f[i]==f[i+1]:
            c+=1
        else:
            mx=max(mx,c)
            c=1
    if c>mx:
        mx=c
    e=f[-1]
    x=0
    for i in range(len(f)-1,-1,-1):
        if f[i]==e:
            x+=1
        else:
            break
    d=[]
    d.append(mx)
    for i in range(b):
        e=f[-1]
        v=input()
        if v==e:
            x+=1
        else:
            x=1
        if x>mx:
            d.append(x)
            mx=x
        else:
            d.append(mx)
        f+=v
    print(d)
            
