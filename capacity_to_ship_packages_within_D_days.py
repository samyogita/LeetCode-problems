class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid):
            if mid < max(weights):
                return False
            weight_taken = 0
            days_taken = 1
            for x in weights:
                weight_taken += x
                if weight_taken > mid:
                    days_taken += 1 
                    weight_taken = x
            return days_taken <= days

        l = 0
        r = sum(weights)
        while l < r:
            mid = (l+r) // 2
            if check(mid):
                r = mid
            else:
                l = mid +1
        
        
        return l


        
