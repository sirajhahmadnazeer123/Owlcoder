n=int(input())
for i in range(n):
    d=int(input())
    s=list(map(int,input().split()))
    c=0
    while(sum(s)!=0):
        for i in range(0,len(s),2):
            c+=s[i]-s[i+1]
            s[i]=0
            s[i+1]=0
    print(c)
            
