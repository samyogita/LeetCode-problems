class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:        
        events.sort()
        n = len(events)
        s = [start for start, end, value in events]
        dp = [[-1] * n for _ in range(k + 1)]
        
        def dfs(i, cnt):
            if cnt == 0 or i == n:
                return 0
            if dp[cnt][i] != -1:
                return dp[cnt][i]

            
            idx = bisect_right(s, events[i][1])
            dp[cnt][i] = max(dfs(i + 1, cnt), events[i][2] + dfs(idx, cnt - 1))
            return dp[cnt][i]
        
        return dfs(0, k
