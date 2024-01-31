import numpy as np
class Solution(object):
    def matrixSum(self, nums):
        f=0
        while(len(nums[0])>0):
            c=[]
            for i in nums:
                p=max(i)
                c.append(p)
                i.pop(i.index(p))
            f+=max(c)
        return f
        
