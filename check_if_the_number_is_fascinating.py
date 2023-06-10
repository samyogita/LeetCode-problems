class Solution:
    def isFascinating(self, n: int) -> bool:
        val = str(n) + str(2*n) + str(3*n)
        ans = list(val)
        ans.sort()
        if ans == ['1','2','3','4','5','6','7','8','9']:
            return True
        return False
        
