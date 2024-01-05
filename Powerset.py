s="abc"
n=[]
for i in range(0,len(s)+1):
    for j in range(i+1,len(s)+1):
        n.append(s[i:j])
print(n)
