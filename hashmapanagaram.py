def return_hash(s,t):
    d={}
    h={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in t:
        if i in h:
            h[i]+=1
        else:
            h[i]=1
    c=0
    for key in d:
        if key in h:
            if d[key]>h[key]:
                c+=d[key]-h[key]
        else:
            c+=d[key]
    return c
a="hejfkdlpoeipoejjk"
b="hejfkdlpoeipoeppp"
print(return_hash(a,b))
