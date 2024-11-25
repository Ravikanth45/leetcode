class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        for i in (bin(n)[2:len(bin(n))]):
            if i=="1":
                c=c+1
        return c
        