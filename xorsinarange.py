n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    s=[]
    b,c=map(int,input().split())
    a=x[b]
    print(a)
    for i in range(b+1,c+1):
        a=a&x[i]
        print(x[i])
    print(a)
