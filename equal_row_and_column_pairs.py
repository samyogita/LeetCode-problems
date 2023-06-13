from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        rows = Counter(tuple(i) for i in grid)
        for c in range(len(grid)):
            cols = [grid[i][c] for i in range(len(grid))]
            cnt += rows[tuple(cols)]
        return cnt
