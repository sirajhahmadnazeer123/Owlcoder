s=input().lower()
a='abcdefghijklmnopqrstuvwxyz'
f=[]
for i in s:
    if i in a:
        if i not in f:
            f.append(i)
if len(f)==len(a):
    print(True)
else:
    print(False)
print(f)
print(len())
print(len(s))
print(s)
