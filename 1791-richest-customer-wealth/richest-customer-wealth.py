class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        res = 0
        for i in accounts:
            sm = 0
            for j in i:
                sm+=j
            res = max(res,sm)
        return res


        