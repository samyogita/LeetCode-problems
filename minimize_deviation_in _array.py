from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sl = SortedList()
        for i in nums:
            if i % 2 != 0:
                sl.add(i*2)
                continue
            sl.add(i)
        res = sl[-1] - sl[0]
        while sl[-1] % 2 == 0:
            sm = sl[-1] // 2
            sl.pop(-1)
            sl.add(sm)
            res = min(res, sl[-1] - sl[0])
        return res
