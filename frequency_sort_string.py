class Solution(object):
    def frequencySort(self, s):
        l,f=[],""
        for i in set(s):
            l.append((s.count(i),i))
        l.sort()
        for i in l[::-1]:
            f+=i[1]*i[0]
        return f
