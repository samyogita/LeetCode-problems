from collections import defaultdict
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            g[u].append([v, succProb[i]])
            g[v].append([u, succProb[i]])
        
        pq = [(-1, start)]
        vis = set()
        while pq:
            p, node = heapq.heappop(pq)
            vis.add(node)

            if node == end:
                return p * -1
            
            for child, prob in g[node]:
                if child not in vis:
                    heapq.heappush(pq, (prob*p, child))
        return 0
