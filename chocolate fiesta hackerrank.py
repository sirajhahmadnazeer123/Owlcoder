mod=1000000000+7
def get_even(n):
    return ((2**n)-1)%mod
def get_odd(n):
    return (2**(n-1)-1)%mod
def solve(a):
    # Write your code here
    e=0
    o=0
    d=0
    f=0
    for i in a:
        if i&1:
            o+=1
        else:
            e+=1
    if e!=0:
        d=get_even(e)
    if o!=0:
        f=get_odd(o)
    s=d%mod+f%mod+(d*f)%mod
    return int(s%mod)
f=list(map(int,input().split()))
print(int(solve(f)))
