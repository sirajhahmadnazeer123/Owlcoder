def get_fact(n):
    p=1
    for i in range(2,n+1):
        p*=i
    return p
def get_table(n,i):
    return get_fact(n)//(get_fact(n-i)*get_fact(i))
n=int(input())
s=[]
for i in range(0,n//2+1):
    s.append(get_table(n,i))
print(s)
        
        
