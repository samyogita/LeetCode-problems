class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def find_cost(val):
            return sum(abs(val - num) * c for num, c in zip(nums, cost))

        l, r = min(nums), max(nums)
        ans = find_cost(nums[0])

        while l < r:
            mid = (l+r)// 2
            c1 = find_cost(mid)
            c2 = find_cost(mid+1)
            ans = min(c1,c2)

            if c1 > c2:
                l = mid+1
            else:
                r = mid
        return ans
