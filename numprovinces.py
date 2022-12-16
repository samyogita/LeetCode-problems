from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        vis = set()
        n = len(isConnected)
        g = defaultdict(list)
        def dfs(node):
            vis.add(node)
            for x in g[node]:
                if x not in vis:
                    dfs(x)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    g[i].append(j)
        for k in range(n):
            if k not in vis:
                count += 1
                dfs(k)
        return count