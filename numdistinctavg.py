class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = set()
        avg = 0
        for i in range(1, len(nums)):
            avg = (nums[i-1] + nums[len(nums)-i]) / 2
            res.add(avg)
        print(res)
        return len(res)
            