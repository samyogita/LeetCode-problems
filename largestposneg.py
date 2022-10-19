class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = []
        res =[]
        for i in nums:
            if i < 0:
                neg.append(int(i))
        
        for i in neg:
            if abs(i) in nums:
                res.append(abs(i))
            
        return(max(res) if res else -1)
                