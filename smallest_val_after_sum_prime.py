class Solution:
    def smallestValue(self, n: int) -> int:
        def get_prime(n):
            res = 0
            start = 2
            while start * start <= n:
                if n % start:
                    start += 1
                    continue
                while n % start == 0:
                    n /= start
                    res += start
                start += 1
            if n > 1:
                res += n
            return res
        
        while(get_prime(n)) != n:
            n = get_prime(n)
        
        return int(n)