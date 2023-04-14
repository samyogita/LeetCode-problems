class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def lps(l, r):
            if l >= r:
                return int(l == r)
            if s[l] == s[r]:
                return 2 + lps(l+1, r-1)
            return max(lps(l+1,r), lps(l, r-1))
        return lps(0, len(s)-1)
