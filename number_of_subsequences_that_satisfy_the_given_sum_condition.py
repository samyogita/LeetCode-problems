class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        res = l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + (1 << (r - l) ) % MOD ) % MOD
                l += 1
            else:
                r -= 1
        return res
