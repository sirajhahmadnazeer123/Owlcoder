# cook your dish here
n=int(input())
for _ in range(n):
    a=int(input())
    c=a
    cnt=0
    while(c):
        cnt+=1
        c//=2
    f=(1<<(cnt-1))
    g=a^f
    print(g,f)
