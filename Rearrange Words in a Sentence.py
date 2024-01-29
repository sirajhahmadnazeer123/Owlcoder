class Solution:
    def arrangeWords(self, text: str) -> str:
        s=[]
        d=""
        for i in text.split():
            s.append(i)
        s=sorted(s, key=len)
        print(s)
        for i in range(0,len(s)):
            if i==0:
                d+=s[i].capitalize()
                d+=" "
            else:
                d+=s[i].lower()
                d+=" "
        return d[:-1]
