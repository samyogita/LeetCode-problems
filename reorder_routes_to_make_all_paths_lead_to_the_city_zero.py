from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        vis = set()
        g = defaultdict(list)

        def dfs(node):
            vis.add(node)
            for i, x in g[node]:
                if i not in vis:
                    self.res += x
                    dfs(i)

        for u, v in connections:
            g[u].append((v,1))
            g[v].append((u,0))
        
        dfs(0)

        return self.res
