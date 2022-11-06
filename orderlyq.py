class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        res = s
        l = len(s)
        if k >= 2:
            s = sorted(s)
            return("".join(s)) 
        if k == 1:
            for i in range(0, len(s)):
                ans = s[1:] + s[0]
                s = ans
                res = min(res, ans)
            return res
        