class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[-1 for _ in range(len(word2)+1)]for _ in range(len(word1)+1)]
        
        def minDis(i, j, dp):
            if i == 0:
                return j
            if j == 0:
                return i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            
            elif word1[i-1] == word2[j-1]:
                dp[i][j] =  minDis(i-1, j-1,dp)
                
            elif word1[i-1] != word2[j-1]:
                dp[i][j] = 1 + min(minDis(i-1, j, dp),minDis(i, j-1, dp), minDis(i-1, j-1, dp))
            
            return dp[i][j]
            
        return minDis(len(word1), len(word2), dp)
            