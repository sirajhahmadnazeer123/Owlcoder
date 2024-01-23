class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        n=len(arr)
        p = 1 << n
        v = []
        for i in range(0, p):
            s=""
            subset = []
            for j in range(0, n):
                if i & (1 << j):
                    subset.append(arr[j])
            s="".join(subset)
            if len(list(s))==len(set(s)):
                v.append(len(s))
        return max(v)

        
