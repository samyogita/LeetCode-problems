class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            dir = [1,0,-1,0,1]
            vis.add((x,y))
            cur = 4
            for i  in range(4):
                nx, ny = x + dir[i], y + dir[i+1]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    cur -= 1
                    if (nx, ny) not in vis:
                        cur += dfs(nx,ny)
            return cur

        m = len(grid)
        n = len(grid[0])
        vis = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i,j)