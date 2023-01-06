class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        mp = {}
        nums.sort(reverse=True)
        mx = 0
        for i in nums:
            mp[i] = mp.get(i*i, 0) + 1
            mx = max(mx, mp[i])
        
        if mx < 2:
            return - 1
        return mx
        