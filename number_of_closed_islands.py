class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cnt = 0 
        m = len(grid)
        n = len(grid[0])
        dir = [1,0,-1,0,1]

        def dfs(x,y):
            ok = True
            grid[x][y] = 1
            for i in range(4):
                nx, ny = x + dir[i], y + dir[i+1]
                if 0 <= nx < m and 0 <=ny < n:
                    if grid[nx][ny] == 0:
                        ok &= dfs(nx,ny)
                else:
                    ok = False
            return ok
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += dfs(i, j)
                    
        return cnt
