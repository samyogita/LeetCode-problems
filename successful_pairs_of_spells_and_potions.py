class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        
        potions = sorted(potions)
        for s in spells:
            count = 0
            
            x = ceil(success/s)
            count = len(potions) - bisect_left(potions,x)
            res.append(count)
            
        return res
