class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        vis = set()
        res = 0
        g = defaultdict(list)
        n = len(strs)
        def dfs(node):
            vis.add(node)
            for child in g[node]:
                if child not in vis:
                    dfs(child)

        for i in range(n):
            for j in range(i+1,n):
                cnt = 0
                for a,b in zip(strs[i], strs[j]):
                    cnt += (a != b)
                    
                if cnt <= 2:
                    g[i].append(j)
                    g[j].append(i)

        for x in range(n):
            if x not in vis:
                res += 1
                dfs(x)
        return res
