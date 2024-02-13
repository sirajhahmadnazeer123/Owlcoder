class Solution:
    def dayOfYear(self, date: str) -> int:
        c=0
        month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        leap_year=[1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016]
        s=date[5:7]
        if s[0]=="0":
            s=s[1]
        if s=="1":
            d=date[8:10]
            return int(d)
        s=int(s)
        for i in range(1,s+1):
            if i in month_days:
                c+=month_days[i]
        c=c-(month_days[s]-int(date[8:10]))
        year=int(date[0:4])
        if year in leap_year and s>2:
            return c+1
        return c
