class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        cnt = 0
        j = 0
        for i in range(len(s)):
            f = False
            p = s[i]
            j = i + 1
            while j < len(s):
                if p == s[j]:
                    if f:
                        break
                    f = True
                p = s[j]
                j += 1
            cnt = max(cnt, j-i)
            
            
        return cnt
