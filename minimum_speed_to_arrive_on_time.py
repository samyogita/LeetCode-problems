class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour < len(dist) - 1:
            return -1

        l, r = 1, 10**7
        ans = -1

        while l <= r:
            m = (l + r) // 2
            if self.check(dist, hour, m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans

    def check(self, dist: List[int], hour: float, speed: int) -> bool:
        time = 0.0
        i = 0
        while time <= hour and i < len(dist) - 1:
            time += math.ceil(dist[i] / speed)
            i += 1

        time += dist[-1] / speed
        return time <= hour￼Enter
