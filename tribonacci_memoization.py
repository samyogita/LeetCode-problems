class Solution:
    def tribonacci(self, n: int) -> int:
        # Memoization
        dp = [-1] * (n + 1)
        def fib(n):
            if n == 0 or n == 1:
                return n
            elif n == 2:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            dp[n] = fib(n-1) + fib(n-2) + fib(n-3)
            return dp[n]
        return fib(n)