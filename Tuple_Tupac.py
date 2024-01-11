def get_prime_Tuple(n):
    d=[1]*(n)
    d[0]=0
    d[1]=0
    cnt=0
    for i in range(2,int(n**0.5)+1):
        if d[i]==1:
            for j in range(i*i,n,i):
                d[j]=0
    s=[]
    for i in range(len(d)):
        if d[i]==1:
            s.append(i)
    g=[]
    for i in range(0,len(s)-1):
        for j in range(i,len(s)-1):
            if i not in g:
                if (s[i]+s[j]) in s:
                    cnt+=1
    return s
n=11
print(get_prime_Tuple(n))
