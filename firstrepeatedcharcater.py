def nonrepeatingCharacter(s):
    g={}
    for i in s:
        if i in g:
            g[i]+=1
            if g[i]==2:
                return i
        else:
                g[i]=1
    return g
g=input()
print(nonrepeatingCharacter(g))
    
