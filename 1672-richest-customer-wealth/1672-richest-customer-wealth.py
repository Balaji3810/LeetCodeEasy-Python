class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxW = 0
       
        for i in range(len(accounts)):
            temp = 0
            for j in range(len(accounts[i])):
               temp = temp + accounts[i][j]
            maxW = max(maxW, temp)   
        return maxW
              