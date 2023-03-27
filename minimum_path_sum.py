class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
                    continue
                elif x == 0:
                    grid[x][y] += grid[x][y-1]
                elif y == 0:
                    grid[x][y] += grid[x-1][y]
                else:
                    grid[x][y] += min(grid[x-1][y],grid[x][y-1])

        return grid[x][y]


