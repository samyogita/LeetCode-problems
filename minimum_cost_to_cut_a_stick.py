class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        @cache
        def dp(l,r):
            if r-l+1 < 3:
                return 0
            res = float('inf')
            for i in range(l+1,r): 
                res =  min(res, (cuts[r] - cuts[l]) + dp(l,i) + dp(i,r)) 
            return res    
        return dp(0, len(cuts)-1)
