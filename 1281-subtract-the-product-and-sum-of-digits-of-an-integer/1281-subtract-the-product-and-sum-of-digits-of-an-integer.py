class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        p=1
        r=0
        while n>0:
            r=n%10
            s=s+r
            p=p*r
            n=n//10
        return p-s