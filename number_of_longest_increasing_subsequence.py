class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        cnt = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        cnt[i] = 0
                    if length[j] + 1 == length[i]:
                        cnt[i] += cnt[j]
        
        max_length = max(length)
        res = 0
        
        for i in range(n):
            if length[i] == max_length:
                res += cnt[i]
        
        return res
