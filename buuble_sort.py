def get_bubble_recur(i,arr,n):
    if n==0:
        return 0
    if(i==n-1):
        get_bubble_recur(0,arr,n-1)
        return
    if (arr[i]>arr[i+1]):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    get_bubble_recur(i+1,arr,n)
    return
h=[2,1,3,4,7,1,6,9,4]
get_bubble_recur(0,h,9)
print(h)
