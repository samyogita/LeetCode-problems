class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        @cache
        def dp(x):
            if x == k-1:
                return min(n-k+1,maxPts)/maxPts
            elif x >= k:
                return x <= n
            return (dp(x+1)-dp(x+maxPts+1))/maxPts + dp(x+1)

        return dp(0)
