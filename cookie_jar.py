for i in range(int(input())):
    a,b=map(int,input().split())
    f=list(map(int,input().split()))
    for i in range(0,a-1):
        if f[i]<b:
            f.pop(i)
    g=[]
    if len(f)==0:
        print(-1)
    else:
        for i in f:
            g.append(i%b)
    print(min(g))
