N=int(input())
f=0
d=bin(N)
d=d[2:]
print(d)
print(len(d))
for i in range(1,len(d)+1):
    if  N&i:
        print(N&i)
    else:
        f=0
        break
if f==1:
    print(1)
else:
    print(0)
                                      
