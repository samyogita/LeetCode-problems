class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                g[manager[i]].append(i)
        res = 0
        def dfs(node, cur):
            nonlocal res
            res = max(res, cur)
            for child in g[node]:
                dfs(child, cur + informTime[node])
        dfs(headID, 0)
        return res
