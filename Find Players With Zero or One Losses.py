def iteerate(li):
    v=[]
    b=[]
    j=[]
    d ={}
    k={}
    for i in range(len(li)):
        if li[i][0] in d:
            d[li[i][0]]+=1
        else:
            d[li[i][0]]=1
    for i in range(len(li)):
        if li[i][1] in k:
            k[li[i][1]]+=1
        else:
            k[li[i][1]]=1
    for i in d:
        if i not in k:
            v.append(i)
    v.sort()
    for i in k:
        if k[i]==1:
            b.append(i)
    b.sort()
    j.append(v)
    j.append(b)
    return j
    
    
li=[[2,3],[1,3],[5,4],[6,4]]
print(iteerate(li))
            
