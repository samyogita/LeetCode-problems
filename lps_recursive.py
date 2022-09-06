class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lps(s, l, r):
            if l >= r:
                if l == r:
                    return 1
                else:
                    return 0
            
            if s[l] == s[r]:
                return 2 + lps(s, l+1, r-1)
            else:
                return max(lps(s, l, r-1), lps(s, l+1, r))
            
        return lps(s, 0, len(s)-1)
        
        
        