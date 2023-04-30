class DSU:
    def __init__(self,n):
        self.comp = n-1
        self.rep = [*range(n)]
        self.sz = [1] * n

    def find(self,u):
        if u != self.rep[u]:
            self.rep[u] = self.find(self.rep[u])
        return self.rep[u]
    
    def merge(self,u,v):
        u, v = self.find(u), self.find(v)
        if u == v:
            return True
        self.comp -= 1
        if self.sz[v] > self.sz[u]:
            u, v = v, u
        self.rep[v] = u
        self.sz[u] += self.sz[v]
        return False
    

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a = DSU(n+1)
        b = DSU(n+1)
        res = 0
        
        for t,u,v in edges:
            if t == 3:
                res += a.merge(u,v)
                b.merge(u,v)

        for t,u,v in edges:
            if t == 2:
                res += b.merge(u,v)
            elif t == 1:
                res += a.merge(u,v)

        return -1 if a.comp > 1 or b.comp > 1 else res
