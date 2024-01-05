def lengthOfLIS(nums):
        m=len(nums)
        d=[1]*m
        for i in range(0,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    d[i]=max(d[i],d[j]+1)
        return max(d)
n=list(map(int,input()).split())
print(lengthOfLIS(n))
