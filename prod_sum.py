class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = []
        prod = 1
        add = 0
        res = 0
        n = str(n)
        for i in range(len(n)):
            num.append(n[i])
        for n in num:
            add = int(n) + add
        for n in num:
            prod = prod * int(n)
        res = prod - add
        return res
        
            
        