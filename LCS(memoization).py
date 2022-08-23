class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        def lcs(a, b, i, j, dp):
            if i == 0 or j == 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if a[i-1] == b[j-1]:
                dp[i][j] =  1 + lcs(a, b, i-1, j-1, dp)
            else:
                dp[i][j] = max(lcs(a, b, i, j - 1, dp), lcs(a, b, i - 1, j, dp))
                 
            return dp[i][j]
        
        return lcs(text1, text2, len(text1), len(text2), dp)