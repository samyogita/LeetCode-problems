class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        rem = 0
        res = []
        for i in word:
            i = int(i)
            rem = (rem * 10 + i) % m
            if rem == 0:
                res.append(1)
            else:
                res.append(0)
        return res
