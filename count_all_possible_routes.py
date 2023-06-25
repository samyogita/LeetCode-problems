class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(cur, rem):
            if rem < 0:
                return 0
            elif cur == finish:
                res = 1
            else:
                res = 0
            
            for i in range(len(locations)):
                if cur != i:
                    cst = abs(locations[cur]-locations[i])
                    res += dp(i, rem-cst)
            return res % MOD
        return dp(start, fuel)                
