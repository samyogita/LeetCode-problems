class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        res = 0
        @cache
        def dp(digits):
            if digits > high:
                return 0
            res = (digits>=low)
            res += dp(digits+zero)
            res += dp(digits+one)
            return res % MOD
        return dp(0)
        
