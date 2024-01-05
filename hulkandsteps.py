n=int(input())
for i in range(n):
    a=int(input())
    c=0
    while(a):
        c+=a&1
        c>>=1
    print(c)        
