# cook your dish here
import math
k=int(input())
for i in range(k):
    a,b=map(int,input().split())
    l=[]
    for i in range(1,a+1):
        l.append(i)
    if a==b:
        print(*l)
    elif b>(a//2):
        d=[]
        for i in range(1,b+1):
            d.append(i)
        print(*d)
    else:
        s=[]
        for i in range(1,b+1):
            s.append((a//b)*(i))
        print(*s)
            
