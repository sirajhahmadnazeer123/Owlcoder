class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = "abcdefghijklmnopqrstuvwxyz"
        c = ""
        for i in s:
            c += str(a.index(i) + 1)
        while k!=0:
            z = 0
            for i in c:
                z += int(i)
            c = str(z)
            k-=1
        return int(c)
