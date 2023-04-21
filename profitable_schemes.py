class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dp(n,i, profits):
            if i == len(group):
                return profits >= minProfit
            exclude = dp(n, i+1, profits)
            include = 0
            if n >= group[i]:
                include = dp(n-group[i],i+1,min(minProfit, profit[i]+profits))
            return (include+exclude) 
        return dp(n,0,0) % MOD
            
