    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s=""
        r=0
        n=abs(num)
        while n!=0:
            r=n%7
            n//=7
            s=str(r)+s
        if num>0:
            return s
        elif num==0:
            return 0
        else:
            return "-"+s
