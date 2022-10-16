class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev = []
        for i in nums:
            if i < 9:
                rev.append(i)
            else:
                i = str(i)
                i = i[::-1]
                rev.append(int(i))
        ans = set(rev + nums)
        return(len(ans))