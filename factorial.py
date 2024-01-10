n = 1000
l = [1]
for i in range(2,n+1):
    for j in range(len(l)):
        d=l[j]*i
        l[j]=d
print(l)
        
        
