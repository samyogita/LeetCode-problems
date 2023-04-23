class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        MOD = 10 **9 + 7 
        @cache
        def dp(index):
            res = 0
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            for i in range(index,len(s)):
                cur = int(s[index:i+1])
                if cur > k:
                    break
                res += dp(i+1)
                res %= MOD
            return res

        return dp(0)
