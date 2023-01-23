class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        n = str(n)
        for i in range(len(n)):
            if i == 0:
                total += int(n[i])
            elif i % 2 != 0:
                total -= int(n[i])
            else:
                total += int(n[i])
        return total
                