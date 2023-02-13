class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + high % 2 + low %2 ) // 2

        
