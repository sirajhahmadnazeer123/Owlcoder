words1 =["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]
p=[]
for i in words1:
    c=1
    for j in range(0,len(words2)):
        l=words2[j]
        for k in l:
            if k not in i:
                c=0
                break
    if c!=0:
        p.append(i)
print(p)
