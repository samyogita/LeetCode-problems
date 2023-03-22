from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        vis = set()
        res = float('inf')

        def dfs(node):
            nonlocal res
            vis.add(node)
            for v,d in g[node]:
                if v not in vis:
                    dfs(v)
                res = min(res, d)
            return res

        for u,v,d in roads:
            g[u].append((v,d))
            g[v].append((u,d))
        
        
        return dfs(1)
