class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minDis(word1, word2, i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            elif word1[i-1] == word2[j-1]:
                return minDis(word1, word2,i-1, j-1)
            elif word1[i-1] != word2[j-1]:
                return 1 + min((minDis(word1, word2,i-1, j),minDis(word1, word2,i, j-1), minDis(word1, word2,i-1, j-1)))
            
        return minDis(word1, word2, len(word1), len(word2))
            
        