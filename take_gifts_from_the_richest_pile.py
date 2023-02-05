import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []
        res = 0
        for x in gifts:
            heapq.heappush(pq, -x)
        for i in range(k):
            maxele = - 1 * heapq.heappop(pq)
            heapq.heappush(pq, - 1 * math.floor(math.sqrt(maxele)))
        for j in pq:
            res += abs(j)
        return res

