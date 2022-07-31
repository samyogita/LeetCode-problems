import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l , r = 1, max(piles)
        
        while l< r: 
            mid = (l+r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / mid)
            if hours <= h:
                
                r = mid
            else:
                l = mid + 1
        return l
                
                
                