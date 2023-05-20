from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(dict)
        res = []
        for (a,b), v in zip(equations, values):
            g[a][b] = v
            g[b][a] = 1 / v
            g[a][a] = 1
            g[b][b] = 1
        
        for i,j in queries:
            vis = set()
            q = deque([])
            if i in g:
                q.append((i,1))
            ans = -1
            while q:
                cur, val = q.popleft()
                if cur == j:
                    ans = val
                    break
                for n in g[cur]:
                    if n not in vis:
                        vis.add(n)
                        g[i][n] = g[i][cur] * g[cur][n]
                        q.append((n, g[i][n]))
            res.append(ans)   
        return res
