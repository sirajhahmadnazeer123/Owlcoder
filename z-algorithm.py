n=input()#input string
pat=input()#pattern
joinn=pat+'$'+n #combination of both the strings
coun=0
i=0
j=1
z=[]
c=[]
while(j<len(joinn)):
    
    if(joinn[i]==joinn[j]):#comparing each element with every other element
        coun+=1
        j+=1
        i+=1
        continue
    else:
        z.append(coun)
        coun=0
        j-=i
        i=0
        
    j+=1

if(joinn[j-len(pat):]==pat):#checking for the last substring of size of pattern
    z.append(len(pat))

print ("the occurences of pattern is at positions: ",end=' ')
for i in range(len(z)):
    if(z[i]==len(pat)):
        c.append(i-len(pat)+1)
print(c)
#code by
#karan mittal
