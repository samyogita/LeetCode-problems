class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        pre = [0]
        rev = nums[::-1]
        suf = [0]
        res = []
        n = len(nums)
        for i in range(len(nums)-1):
            pre.append(pre[-1]+nums[i])
        for j in range(len(rev)-1):
            suf.append(suf[-1]+rev[j])
        suf = suf[::-1]
        zipped = zip(pre, suf)
        for r,s in zipped:
            res.append(abs(r-s))
        return res
        
        
