class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction = sorted(satisfaction)
        res = 0

        for i in range(len(satisfaction)):
            cur = 0
            for j in range(i,len(satisfaction)):
                cur += (j-i+1)*satisfaction[j]

            res = max(res, cur)

        return res
