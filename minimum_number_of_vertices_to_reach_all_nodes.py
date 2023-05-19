from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indeg = [0] * n
        for u, v in edges:
            indeg[v] += 1
        return [i for i in range(len(indeg)) if indeg[i] == 0]
