class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def backtrack(pairs, mask):
            if pairs * 2 == len(nums):
                return 0
            res = 0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if mask & (1 << i) or mask & (1 << j):
                        continue
                    nmask = mask | 1 << i | 1 << j
                    cur = (pairs+1) * math.gcd(nums[i], nums[j])
                    cur += backtrack(pairs+1,nmask)
                    res = max(res, cur)
            return res
        return backtrack(0,0) 
