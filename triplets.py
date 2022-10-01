class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        c = 0
        for i in range (len(nums)):
            if (nums[i] + diff) in nums and (nums[i]+diff+diff) in nums:
                c += 1
        return c