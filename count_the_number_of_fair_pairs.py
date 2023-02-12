class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, j in enumerate(nums):
            a, b = bisect_left(nums, lower-j, i+1), bisect_right(nums, upper-j, i+1)
            ans += b - a
        return ans
        
