class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        add = 0
        banned = set(banned)
        for i in range(1, n+1):
            if i not in banned:
                add += i
                if add > maxSum:
                    break
                res += 1
        return res
        