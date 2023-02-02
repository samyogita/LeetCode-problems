class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] 
        for x in nums:
            res.append(res[-1]+ x)
        return res[1:]