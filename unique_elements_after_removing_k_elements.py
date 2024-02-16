class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        s = dict(sorted(d.items(), key=lambda item: item[1]))
        unique_ints_count = len(s)
        for count in s.values():
            if k >= count:
                k -= count
                unique_ints_count -= 1
            else:
                break

        return unique_ints_count
