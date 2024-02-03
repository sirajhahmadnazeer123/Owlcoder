def get_median(arr,arr1):
    l=sorted(arr+arr1)
    d=len(l)
    if d%2!=0:
        return l[(d//2)]
    else:
        return ((l[(d//2)-1]+l[(d//2)])/2)
k=[1,3]
p=[2,4]
print(get_median(k,p))
