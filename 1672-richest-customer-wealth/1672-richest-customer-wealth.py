class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ac=[]
        for i in range(len(accounts)):
            ec=0
            for j in range(len(accounts[i])):
                ec+=accounts[i][j]
            ac.append(ec)
        return max(ac)