class Solution:
    def longestPalindrome(self, s: str) -> int:
        f=0
        c=0
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]%2==0:
                c+=d[i]
            elif f==0 and d[i]%2!=0:
                c+=d[i]
                f=1
            else:
                c+=d[i]-1
        return c
