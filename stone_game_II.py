class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf = [0]
        for i in range(n-1,-1,-1):
            suf.append(suf[-1]+piles[i])
        suf.reverse()
        @cache
        def dp(idx, m):
            if idx + 2 * m >= n:
                return suf[idx]
            res = 0
            for i in range(1, 2*m+1):
                res = max(res, suf[idx] - dp(idx+i,max(i,m)))
            return res
        return dp(0,1)
