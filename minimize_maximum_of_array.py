class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def solve(mid):
            cur = 0
            for i in nums:
                cur += mid - i
                if cur < 0:
                    return False
            return True

        l = 0
        r = max(nums)
        while l < r:
            mid = (l+r) // 2
            if solve(mid):
                r = mid
            else:
                l = mid + 1
        return l
                
           
            
        
