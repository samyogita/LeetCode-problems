class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        cnt = 0
        res = 0
        m = len(grid)
        n = len(grid[0])
        dir = [1,0,-1,0,1]

        def dfs(x,y):
            nonlocal cnt
            cnt += 1
            ok = True
            grid[x][y] = 0
            
            for i in range(4):
                nx, ny = x + dir[i], y + dir[i+1]
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        ok &= dfs(nx,ny)
                else:
                    ok = False
            return ok
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = 0
                    if dfs(i, j):
                        res += cnt
        return res
                        
