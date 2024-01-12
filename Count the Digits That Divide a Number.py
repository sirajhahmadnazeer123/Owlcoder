num=1248
temp=num
c=0
while(temp>0):
    r=temp%10
    if num%r==0:
        c+=1
    temp//=10
print(c)
        
