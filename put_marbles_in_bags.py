class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pw = [0] * (len(weights) - 1)
        for i in range(len(weights) - 1):
            pw[i] = weights[i] + weights[i + 1]
        pw.sort()
        res = 0
        for i in range(k - 1):
            res += pw[len(weights) - 2 - i] - pw[i]
        return res
