def prime(a):
    if a>=2:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
        return True
def prime_fac(a,b):
  f={}
  c=0
  for j in range(a,b+1):
        d=2
        while j>1:
           temp=j
           if prime(d):
               if j%d==0:
                   if d in f:
                       f[d]+=1
                   else:
                       f[d]=1
               j=temp//d
           else:
              d+=1
  for i in f:
      c+=f[i]
  return c
a,b=map(int,input().split())
print(prime_fac(a,b))
        
