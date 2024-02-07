class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        d=[]
        for i in sentence.split():
            d.append(i)
        for i in dictionary:
            s=len(i)
            for j in range(len(d)):
                g=d[j]
                if len(g)>=len(i):
                    if g[:s]==i:
                        d[j]=i
        return " ".join(d)
