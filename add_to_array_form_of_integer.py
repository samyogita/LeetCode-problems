class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if k == 0:
            return num
        val = ''
        ans = 0
        for i in num:
            val += str(i)
        ans = int(val) + k
        res = list(map(int, str(ans)))
        return res
