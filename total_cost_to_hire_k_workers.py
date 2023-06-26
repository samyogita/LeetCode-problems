class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq = []
        for i in range(candidates):
            pq.append((costs[i],0))
        for j in range(max(candidates, len(costs)-candidates), len(costs)):
            pq.append((costs[j],1))
        heapify(pq)
        ans = 0
        head, tail = candidates, len(costs)-1-candidates

        for x in range(k):
            cost, c_id = heappop(pq)
            ans += cost
            if head <= tail:
                if c_id == 0:
                    heappush(pq, (costs[head],0))
                    head += 1
                else:
                    heappush(pq, (costs[tail],1))
                    tail -= 1
        return ans
