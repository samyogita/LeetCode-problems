class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1 
        n = len(grid)
        dir = [1,-1,-1,1,1,0,-1,0,1]
        q = deque([(0,0)])
        level = 0
        while q:
            nq = []
            for x, y in q:
                if x == n-1 and y == n-1:
                    return level+1
                for j in range(8):
                    nx, ny = x + dir[j], y + dir[j+1]
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        nq.append((nx,ny))
                        grid[nx][ny] = -1
            q = nq
            level += 1
        return -1


                    


            
