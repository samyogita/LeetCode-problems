class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            ans = nums[i]
            for j in range(i, len(nums)):
                ans = lcm(ans, nums[j])
                if ans == k:
                    count += 1
        return count
                    
    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)


    def lcm(a, b):
        return (a / gcd(a, b)) * b
        