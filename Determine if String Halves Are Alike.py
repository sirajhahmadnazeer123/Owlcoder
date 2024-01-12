f="aeiouAEIOU"
def get_half(s):
    s.lower()
    c=0
    p=0
    n=len(s)//2
    j=s[0:n]
    d=s[n:len(s)]
    for i in j:
        if i in f:
            c+=1
    for i in d:
        if i in f:
            p+=1
    if c==p:
        return True
    else:
        return False
s="Uo"
print(get_half(s))
