n=int(input())
for i in range(n):
    v=int(input())
    h=list(map(int,input().split()))
    d=list(map(int,input().split()))
    f=0
    h.sort()
    d.sort()
    d=d[::-1]
    s=max(h)+min(d)
    for i in range(0,v):
        if h[i]+d[i]!=s:
            f=1
            break
    if f!=1:
        print(*h)
        print(*d)
    else:
        print(-1)
