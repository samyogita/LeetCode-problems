class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def dp(l, r):
            if l >= r:
                return int(l==r)
            if s[l] == s[r]:
                return 2 + dp(l+1,r-1)
            return max(dp(l+1,r), dp(l,r-1))
        return len(s) - dp(0, len(s)-1) 
