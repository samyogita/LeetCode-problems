from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        mp = Counter(nums)
        for key, val in mp.items():
            if val == 1:
                return key
