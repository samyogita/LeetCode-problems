class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
        return output
            