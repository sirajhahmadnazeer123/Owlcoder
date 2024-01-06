    def sumOfPowers(self, a : int, b : int) -> int:
        # code here
        
        def sieve():
            for i in range(2, maxn,2) :
                spf[i] = 2 
            for i in range(3, math.ceil(math.sqrt(maxn))):
                if spf[i] == i:
                    for j in range(i, maxn, i):
                        spf[j] = i
            maxn = b+1
            spf = [i for i in range(maxn+1)]
            hmap = defaultdict(int)
            sieve()
        def prime_factorization(num):
            while(num != 1):
                hmap[spf[num]] += 1
                num = num//spf[num]
        # print(spf)
            for i in range(a, b+1):
                prime_factorization(i)
            # print(hmap)
            return sum(hmap.values())
