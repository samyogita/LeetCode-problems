class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high
        for i in range(1, high+1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
        res = 0
        for i in range(low, high+1):
            res += dp[i]
        return res % int(1e9 + 7)
        
