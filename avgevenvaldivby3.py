class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sums, count = 0, 0
        for ele in nums:
            if ele % 3 == 0 and ele % 2 == 0:
                sums += ele
                count += 1
                
        return(int(sums/count)) if sums else 0