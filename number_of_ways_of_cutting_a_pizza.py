class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        m = len(pizza)
        n = len(pizza[0])
        suf = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                suf[i][j] = suf[i][j+1] + suf[i+1][j] - suf[i+1][j+1] + (pizza[i][j] == 'A')
        @cache
        def solve(r,c,rem):
            res = 0
            if rem == 0:
                return suf[r][c] > 0

            for l in range(r+1,m):
                if suf[r][c] - suf[l][c] > 0:
                    res += solve(l,c,rem-1)
            
            for l in range(c+1,n):
                if suf[r][c] - suf[r][l] > 0:
                    res += solve(r,l,rem-1)
            return res

        return solve(0,0,k-1) % MOD
