class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(mid):
            val = 0
            for i in time:
                val += mid // i
            return val 
        l = 0
        r = max(time) * totalTrips
        while l < r:
            mid = (l+r) // 2
            if check(mid) >= totalTrips:
                r = mid
            else:
                l = mid + 1
        return l
