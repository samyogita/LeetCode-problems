class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(range(n) )
        for _, x in edges:
            if x in res:
                res.remove(x)
        return list(res)
