class Solution:
    def minOperations(self, n: int) -> int:
        res = size = 0
        n = list(bin(n))
        n = n[2:]
        n.reverse()
        for r in range(len(n)):
            if n[r] == '1':
                size += 1
            elif size > 1:
                res += 1
                size = 1
            elif size == 1:
                res += 1
                size = 0
        if size > 1:
            res += 1
            size = 1
        if size == 1:
            res += 1
        return res
                
