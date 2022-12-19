class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.found = False
        g = defaultdict(list)
        vis = set()

        def dfs(node):
            if node == destination:
                self.found = True
                return True
            vis.add(node)
            for child in g[node]:
                if child not in vis:
                    dfs(child)
        
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        
        dfs(source)

        return self.found