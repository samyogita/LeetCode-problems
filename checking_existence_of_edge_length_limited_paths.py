class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        rep, sz = list(range(n) ), [1] * n
        def find(u):
            if u != rep[u]:
                rep[u] = find(rep[u])
            return rep[u]
        def merge(u, v):
            u, v = find(u), find(v)
            if u == v:  
                return
            if sz[v] > sz[u]:   
                u, v = v, u
            sz[u] += sz[v]
            rep[v] = u

        edgeList.sort(key=lambda x:x[2])
        queries = sorted( (d, u, v, i) for i, (u, v, d) in enumerate(queries) )
        idx, res = 0, [False] * len(queries)
        for d, u, v, i in queries:
            while idx < len(edgeList) and edgeList[idx][2] < d:
                merge(edgeList[idx][0], edgeList[idx][1])
                idx += 1
            res[i] = find(u) == find(v)
        return res
