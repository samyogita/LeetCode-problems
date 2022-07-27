class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums) ):
            b = target - nums[i]
            if b in pairs:
                return [pairs[b], i]
            else:
                pairs[nums[i]] = i
        