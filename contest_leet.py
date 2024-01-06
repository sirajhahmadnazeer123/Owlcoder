
def missingInteger(nums):
    c=0
    for i in range(0,len(nums)-1):
        if nums[i]<nums[i+1]:
            c+=nums[i]
        else:
            c+=nums[i]
            break
    return c
n=[3,4,5,1,12,14,13]
c=missingInteger(n)
while(True):
        if (c not in n):
            c+=1
        break
print(c)
