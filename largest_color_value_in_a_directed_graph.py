class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        res = -1
        mp = defaultdict(Counter)
        indeg = [0] * len(colors)
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            indeg[v] += 1
        q = deque([i for i in range(len(colors)) if not indeg[i]])
        while q:
            cur = q.popleft()
            mp[cur][colors[cur]] += 1
            res = max(res, mp[cur][colors[cur]])
            for x in g[cur]:
                indeg[x] -= 1
                if indeg[x] == 0:
                    q.append(x)
                for k in mp[cur]:
                    mp[x][k] = max(mp[x][k], mp[cur][k])

        return -1 if max(indeg) > 0 else res
        
            
                
