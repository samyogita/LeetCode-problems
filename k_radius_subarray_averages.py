class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        if k == 0:
            return nums
        if 2 * k + 1 > len(nums):
            return res 
        
        total = sum(nums[:2*k+1])
        res[k] = total // (2*k+1)

        for i in range(2*k+1, len(nums)):
            total = total - nums[i-(2*k+1)] + nums[i]
            res[i-k] = total // (2*k+1)
        
        return res
        
