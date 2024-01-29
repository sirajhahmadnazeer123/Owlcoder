##column to number
class Solution:
    def titleToNumber(self, s: str) -> int:
        c=0
        h=list(s)
        h=h[::-1]
        for i in range(0,len(h)):
            j=ord(h[i])-64
            c+=pow(26,i)*j
        return c
## number to column sheet
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:       
        ans=""        
        while columnNumber>0:
            c=chr(ord('A')+(columnNumber-1)%26)
            ans=c+ans
            columnNumber=(columnNumber-1)//26            
        return ans   
