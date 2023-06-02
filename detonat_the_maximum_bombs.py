from collections import defaultdict 
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = defaultdict(list)
        res = 1
        def dfs(idx, vis):
            if idx in vis:
                return 0
            vis.add(idx)
            for child in g[idx]:
                dfs(child,vis)
            return len(vis)

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x2-x1)**2+(y2-y1)**2)
                if d <= r1:
                    g[i].append(j)
                if d <= r2:
                    g[j].append(i)
                    
        for i in range(len(bombs)):
            res = max(res, dfs(i,set()))
        return res













