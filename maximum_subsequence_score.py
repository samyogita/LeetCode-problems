import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        val = 0
        ans = sorted(zip(nums1,nums2), key=lambda x: -x[1])
        res = [ans[i][0] for i in range(k)]
        heapify(res)
        total = sum(res)
        val = max(val, total*ans[k-1][1])
        for i in range(k, len(nums1)):
            heappush(res, ans[i][0])
            total += ans[i][0]
            popped = heappop(res)
            total -= popped
            val = max(val, total*ans[i][1])
        return val
