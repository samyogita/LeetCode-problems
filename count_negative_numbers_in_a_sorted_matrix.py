class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        n = len(grid[0])
        for row in grid:
            l, r = 0, n-1
            while l <= r:
                mid = (l+r)// 2
                if row[mid] < 0:
                    r = mid - 1
                else: 
                    l = mid + 1
            cnt += (n-l)
        return cnt
