class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        join = '' 
        while len(nums) and len(nums)!= 1:
            first = nums[0]
            last = nums[-1]
            join = str(first) + str(last)
            nums.pop(0)
            nums.pop(-1)
            res += int(join)
        if len(nums) == 0:
            return res
        res += nums[0]
        return res
            
                
                
        
