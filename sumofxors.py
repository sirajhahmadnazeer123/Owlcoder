def trailblazer(n):
    f=1
    for i in range(2,n+1):
        f*=i
    f=str(f)
    return f.count("0")
n=int(input())
print(trailblazer(n))
