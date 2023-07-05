class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            zeros += nums[r] == 0
            while zeros > 1:
                zeros -= nums[l] == 0
                l += 1
            res = max(res, r-l)
        return res
