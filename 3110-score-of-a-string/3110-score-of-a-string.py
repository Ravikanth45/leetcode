class Solution:
    def scoreOfString(self, s: str) -> int:
        l=len(s)
        d=0
        if l>=2 and l<=100:
            for i in range(1,l):
                d+=abs(ord(s[i])-ord(s[i-1]))
        return d
        