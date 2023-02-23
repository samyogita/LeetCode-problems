import heapq 
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        zipped = zip(capital, profits)
        res = sorted(zipped, key = lambda x: x[0])
        i = 0
        pq = [0]
        while pq and k > 0:
            while i < len(res) and res[i][0] <= w:
                heapq.heappush(pq, -res[i][1])
                i+= 1
            w += -1 *heappop(pq)
            k -= 1
        
        return w
