class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        k=1000
        for i in range(1,n*2+1):
            if i%2==0 and i%n==0:
                if k>i:
                    k=i
        return k