def setk(b,a):
    c=((1<<a)|b)
    return c
a,b=map(int,input().split())
print(setk(a,b))
