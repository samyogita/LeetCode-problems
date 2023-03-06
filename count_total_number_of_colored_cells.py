class Solution:
    def coloredCells(self, n: int) -> int:
        n -= 1
        return (2*n*(n+1)+1)
        
