"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def daq(x,y,d):
            if d == 1:
                return Node(grid[x][y], True)
            val = grid[x][y]
            for i in range(d):
                for j in range(d):
                    if grid[x+i][y+j] != val:
                        topLeft = daq(x,y,d//2)
                        topRight = daq(x,y+d//2,d//2)
                        bottomLeft = daq(x+d//2,y,d//2)
                        bottomRight = daq(x+d//2,y+d//2,d//2)
                        return Node(val,False,topLeft, topRight, bottomLeft, bottomRight)
            return Node(grid[x][y], True)
        return daq(0,0,len(grid[0]))
