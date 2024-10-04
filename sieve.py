n=1000002
d=[1]*n
d[0]=0
d[1]=0
for i in range(2,int(n**0.5)+1):
    if d[i]==1:
        for j in range(i*i,n+1,i):
            d[j]=0
    
v=int(input())
for i in range(v):
    b=int(input())
    if d[b]:
        print(1)
    else:
        print(0)

    
import math
a,b=map(int,input().split())
print(math.gcd(a,b))

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime")
else:
    print("Not Prime")
