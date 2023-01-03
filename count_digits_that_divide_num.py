class Solution:
    def countDigits(self, num: int) -> int:
        val = 0
        nums =str(num)
        for i in range(len(nums)):
            if num % int(nums[i]) == 0:
                val += 1
        return val
        