class Solution:
    def titleToNumber(self, s: str) -> int:
        c=0
        h=list(s)
        h=h[::-1]
        for i in range(0,len(h)):
            j=ord(h[i])-64
            c+=pow(26,i)*j
        return c
