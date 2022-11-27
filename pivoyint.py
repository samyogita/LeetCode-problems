class Solution:
    def pivotInteger(self, n: int) -> int:
        val = -1
        for i in range(1, n+1):
            sumx = i *(i+1) / 2
            sumxn = sum(range(i, n+1))
            if sumx == sumxn:
                val = i
        return val
                
            
        