class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minF = maxF = -1
        l = r = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] > maxK or nums[r] < minK:
                l = r + 1
                minF = maxF = -1
            else:
                if nums[r] == minK:
                    minF = r
                if nums[r] == maxK:
                    maxF = r
                if maxF != -1 and minF != -1:
                    res += ((min(minF, maxF))-l) + 1
        return res
                
                