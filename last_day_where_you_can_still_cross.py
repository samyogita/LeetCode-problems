class Solution:
    
    def canCross(self, row, col, cells, day):
        dir = [1,0,-1,0,1]
        grid = [[0] * col for _ in range(row)]
        
        for r, c in cells[:day]:
            grid[r - 1][c - 1] = 1
            
        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] != 0:
                return False
            if x == row - 1:
                return True
            grid[x][y] = -1
            for i in range(4):
                nx, ny = x + dir[i], y + dir[i+1]
                if dfs(nx, ny):
                    return True
            return False
        
        for k in range(col):
            if grid[0][k] == 0 and dfs(0, k):
                return True

        return False
    
    
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l, r = 1, row * col
        
        while l < r:
            mid = r-(r-l) // 2
            if self.canCross(row, col, cells, mid):
                l = mid
            else:
                r = mid - 1
                
        return l
