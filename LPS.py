class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        def lps(s, l, r, dp):
            if l >= r:
                if l == r:
                    return 1
                else:
                    return 0
            if dp[l][r] != -1:
                return dp[l][r]
            
            if s[l] == s[r]:
                dp[l][r] = 2 + lps(s, l+1, r-1, dp)
            else:
                dp[l][r] =  max(lps(s, l, r-1, dp), lps(s, l+1, r, dp))
            
            return dp[l][r]
        return lps(s, 0, len(s)-1, dp)
    