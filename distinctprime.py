class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set()

        def get_prime(n):
            start = 2
            while start * start <= n:
                if n % start != 0:
                    start += 1
                    continue
                while n % start==0:
                    n //= start
                    res.add(start)
                start += 1
            if n > 1:
                res.add(n)
        for i in nums:
            get_prime(i)

        return len(res)