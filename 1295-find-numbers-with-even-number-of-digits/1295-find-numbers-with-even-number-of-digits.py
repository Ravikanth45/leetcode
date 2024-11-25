class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l=[]
        s=0
        for i in nums:
            c=0
            while i>0:
                c+=1
                i=i//10
            l.append(c)
        for i in l:
            if i%2==0:
                s+=1
        return s