from collections import defaultdict
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        res = -1
        vis = set()
        def dfs(node, path):
            nonlocal res
            vis.add(node)
            path.append(node)
            if edges[node] in vis:
                if edges[node] in path:
                    res = max(res, len(path)- path.index(edges[node]))
            elif edges[node] != -1:
                dfs(edges[node],path)
            
        for i in range(len(edges)):
            if i not in vis:
                dfs(i, [])

        return res
