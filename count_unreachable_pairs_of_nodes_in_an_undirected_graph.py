from collections import defaultdict
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        vis = set()
        res = n * (n-1) // 2
        def dfs(node):
            cnt = 1
            vis.add(node)
            for child in g[node]:
                if child not in vis:
                    cnt += dfs(child)      
            return cnt
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        
        for i in range(n):
            if i in vis:
                continue
            cur = dfs(i)
            res -= cur * (cur - 1) // 2
        return res
