class Solution:
    def partitionString(self, s: str) -> int:
        cnt = 0
        mp = set()
        for r in range(len(s)):
            if s[r] not in mp:
                mp.add(s[r])
            else:
                cnt += 1
                mp = set()
                mp.add(s[r])
        return cnt + 1 
