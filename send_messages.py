messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders =  ["Bob","Charlie"]
d={}
for i in range(0,len(senders)):
    if senders[i]  in d:
        c=0
        f=messages[i]
        for j in f.split(" "):
            c+=1
        d[senders[i]]+=c
    else:
        c=0
        f=messages[i]
        for j in f.split(" "):
                c+=1
        d[senders[i]]=c
o=[]
mx=0
for i in d:
    mx=max(d[i],mx)
for i in d:
    if d[i]==mx:
        o.append(i)
print(max(o))
    
