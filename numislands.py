class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        dir = [1,0,-1,0,1]

        def dfs(x,y):
            grid[x][y] = '0'
            for i in range(4):
                nx, ny = x + dir[i], y + dir[i+1]
                if 0 <= nx < m and 0 <= ny < n :
                    if grid[nx][ny] == '1':
                        dfs(nx, ny) 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        return count