class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(k,index):
            if index == len(piles) or k == 0:
                return 0
            exclude = dp(k, index+1)
            include = 0
            res = 0
            for i in range(1, min(k, len(piles[index]))+1):
                res += piles[index][i-1]
                include = max(include, res+dp(k-i, index+1))
            return max(include, exclude)
        return dp(k,0)

