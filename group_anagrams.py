class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hp={}
        for i in strs:
            words="".join(sorted(i))
            if words not in hp:
                hp[words]=[i]
            else:
                hp.get(words).append(i)
        return hp.values()
        
