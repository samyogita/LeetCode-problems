class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        dist = [0] * k

        def bt(i):
            nonlocal ans, dist
            if i == len(cookies):
                ans = min(ans, max(dist))
                return  
            if ans <= max(dist):
                return  
            for j in range(k):
                dist[j] += cookies[i]
                bt(i+1)
                dist[j] -= cookies[i]
        bt(0)
        return ans
