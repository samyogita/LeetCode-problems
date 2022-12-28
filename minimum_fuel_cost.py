from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.res = 0
        g = defaultdict(list)
        vis = set()
        vis.add(0)
        def dfs(node):
            cur = 1
            vis.add(node)
            for child in g[node]:
                if child not in vis:
                    cur += dfs(child)
            self.res += (cur + seats - 1) // seats
            return cur

        for e in roads:
            g[e[1]].append(e[0])
            g[e[0]].append(e[1])
        
        for i in g[0]:
            dfs(i)
        return self.res 