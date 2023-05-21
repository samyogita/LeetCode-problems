class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dir = [1,0,-1,0,1]
        cnt = 0
        def dfs(x,y):
            grid[x][y] = 2
            q.append((x,y))
            for i in range(4):
                nx, ny = x + dir[i], y + dir[i+1]
                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 1:
                        dfs(nx,ny)
        fx, fy = -1, -1
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    fx, fy = x, y
        q = []
        dfs(fx,fy)
        levels = 0
        while q:
            nq = []
            for x,y in q:
                for i in range(4):
                    nx, ny = x + dir[i], y + dir[i+1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return levels
                        elif grid[nx][ny] == 0:
                            nq.append((nx,ny)) 
                            grid[nx][ny] = -1
            q = nq
            levels += 1



            
