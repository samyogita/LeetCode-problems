class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            i = str(i)
            for x in i:
                res.append(int(x))
        return res