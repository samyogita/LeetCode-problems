class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def check(num):
            cnt = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= mid: 
                    cnt += 1
                    i += 1
                i+= 1
            return cnt >= p
     
        l = 0
        r = nums[-1] - nums[0]
        while l < r:
            mid = (l+r) // 2
            if check(mid):
                r = mid
                
            else:
                l = mid + 1
        return l
        
