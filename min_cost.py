class Solution:
	def findMinCost(self, X, Y, costX, costY):
        def longestCommonSubsequence(X, Y) -> int:
            dp = [[0 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]
            for i in range(len(X)):
                dp[i][0] = 0
            for j in range(len(Y)):
                dp[0][j] = 0
            for i in range(1, len(X)+1):
                for j in range(1, len(Y)+1):
                    if X[i-1] == Y[j-1]:
                        dp[i][j] =  1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    
            return dp[-1][-1]
            
        val = longestCommonSubsequence(X, Y)
            
        final = costX * (len(X) - val) +  costY * (len(Y) - val)
        return final    