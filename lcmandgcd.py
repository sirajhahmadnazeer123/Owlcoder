import math
def lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return lcm
a,b=map(int,input().split())
print(lcm(a,b),end=" ")
print(math.gcd(a,b))
