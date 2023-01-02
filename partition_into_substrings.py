class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        m = len(str(k))
        i = res = 0
        while i < n:
            cur  = s[i: min(n, i+m)]
            if int(cur) <= k:
                res += 1
                i = i + m
            else:
                cur = s[i: min(n, i+m-1)]
                if not len(cur):
                    return -1
                else:
                    res += 1
                    i = i + m - 1
        return res