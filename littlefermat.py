mod = 10**9 + 7

def bin_exponent(a, b):
    ans = 1
    while b:
        if b & 1:
            b = b - 1
            ans = (ans % mod)*(a % mod)
        else:
            b = b // 2
            a = (ans % mod)*(a % mod)
    return ans
def inverse(a,p):
    return bin_exponent(a,p-2)
    
a= int(input("Enter n: "))
p= int(input())
u=inverse(a,p)
print(u)


