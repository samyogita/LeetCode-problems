from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        vis = set()
        g = defaultdict(list)
        comp = 0
        if len(connections) < n-1:
            return -1

        def dfs(node):
            nonlocal comp
            vis.add(node)
            for child in g[node]:
                if child not in vis:
                    dfs(child)
        
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        
        for i in range(n):
            if i not in vis:
                comp += 1
                dfs(i)

        return comp - 1 
