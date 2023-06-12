class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:    
            return []    
        res = []
        s, e = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] > e+1:
                if s != e:
                    res.append(str(s)+'->'+str(e))
                else:
                    res.append(str(e))
                s, e = nums[i], nums[i]
            else:
                e = nums[i] 
        if s != e:
            res.append(str(s)+ '->' +str(e))
        else:
            res.append(str(e))
        return res
        

