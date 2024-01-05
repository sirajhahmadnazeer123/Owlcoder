n=15
b=str(bin(n))
b=b[2:]
b=b[::-1]
print(b)
for i in range(0,len(b)):
    if b[i]=="1":
        print(i+1)
        break














    
