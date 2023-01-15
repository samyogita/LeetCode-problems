class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es = sum(nums)
        ds = 0
        for i in nums: 
            i = str(i)
            if len(i) == 1:
                ds += int(i)
            else:
                for j in range(len(i)):
                    ds += int(i[j])
        return (abs(ds-es))
            