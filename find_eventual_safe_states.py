class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indeg = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indeg[i] += 1

        q = deque()
      
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for child in adj[node]:
              
                indeg[child] -= 1
                if indeg[child] == 0:
                    q.append(child)

        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNode
