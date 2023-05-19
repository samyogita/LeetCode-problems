from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)
        def dfs(node,c):
            if color[node]:
                return color[node] == c
            color[node] = c
            for child in graph[node]:
                if not dfs(child, -c):
                    return False
            return True
        
        for i in range(len(graph)):
            if not color[i] and not dfs(i,1):
                return False
        return True
        
