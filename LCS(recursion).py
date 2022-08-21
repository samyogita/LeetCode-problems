class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(text1, text2, i, j):
                if i == 0 or j == 0:
                    return 0
                elif text1[i-1] == text2[j-1]:
                    return 1 + lcs(text1, text2, i-1, j-1)
                else:
                    return max(lcs(text1, text2, i-1, j), lcs(text1, text2, i, j-1))
        return lcs(text1 , text2, len(text1), len(text2))