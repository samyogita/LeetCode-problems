import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        pq = []
        for i in nums:
            heapq.heappush(pq, -i)
        for i in range(k):
            cur = - heappop(pq)
            score += cur
            heappush(pq, -ceil(cur/3))
        return score
        