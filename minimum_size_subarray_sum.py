class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, window_sum = 0, 0
        res = float('inf')
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                res = min(res, r-l+1)
                window_sum -= nums[l]
                l += 1
        return res if res != float('inf') else 0
        
