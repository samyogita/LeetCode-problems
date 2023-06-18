class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        dir = [1,0,-1,0,1]

        @cache
        def dfs(x,y):
            cnt = 1
            for i in range(4):
                nx, ny = x + dir[i], y + dir[i+1]
                if 0 <= nx < m and 0 <= ny < n and(grid[x][y] > grid[nx][ny]):
                    cnt += dfs(nx, ny) % MOD
            return cnt % MOD
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                cnt += + dfs(i, j) % MOD
        return cnt % MOD
