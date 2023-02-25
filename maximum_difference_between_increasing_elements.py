class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        l, r = 0, 1
        while r < len(nums):
            if nums[l] < nums[r]:
                ans = nums[r] - nums[l]
                res = max(res, ans)
            else:
                l = r
            r += 1
                
        return res
