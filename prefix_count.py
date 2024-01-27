s=["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w","gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"]
f="w"
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for word in words:
            n=len(word)
            if s[0:n]==word:
                count+=1
        return count
        
