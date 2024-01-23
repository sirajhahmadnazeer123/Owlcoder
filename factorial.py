def fact(n):
    ##base_case
    if n==0:
        return 1
    ##recursive_case
    return n*fact(n-1)
n=10
print(fact(n))
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    l = fibonacci(n - 1)
    l2 = fibonacci(n - 2)
    return l + l2

l = 10
print(fibonacci(l))
def _sorted(arr,n)->bool:
    if n==0 or n==1:
        return True
    if arr[0]>arr[1]:
        return False
    return _sorted(arr[1:], n - 1)
l=[1,0,2,3,4,5]
n=6
print(_sorted(l,n))
def first_occur(arr,n,k):
    if n==0:
        return -1
    if arr[0]==k:
        return 0
    small=first_occur(arr[1:],n-1,k)
    if small==-1:
        return -1
    else:
        return small+1
def last_occur(arr,n,k):
    if n==0:
        return -1
    small=last_occur(arr[1:],n-1,k)
    if small==-1:
        if arr[0]==k:
            return 0
        else:
            return -1
    else:
        return small+1
        
    
f=[1,2,3,4,5,6,7,7,9]
n=9
k=7
print(first_occur(f,n,k))
print(last_occur(f,n,k))

