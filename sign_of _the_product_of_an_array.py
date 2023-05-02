import numpy
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
            if i == 0:
                return 0
            ans *= i
        return -1 if ans < 0 else 1
