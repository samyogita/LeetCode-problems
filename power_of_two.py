class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ans = False
        if n > 0:
            n &= n-1 
            if n == 0:
                ans = True
        return ans