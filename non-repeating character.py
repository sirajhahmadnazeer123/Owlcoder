def nonrepeatingCharacter(s):
    g={}
    c=0
    for i in s:
        if i in g:
            g[i]+=1
        else:
                g[i]=1
    return max(g.values())
g=input()
print(nonrepeatingCharacter(g))
    
