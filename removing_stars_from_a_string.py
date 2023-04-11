class Solution:
    def removeStars(self, s: str) -> str:
        res = ''
        cnt = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '*':
                cnt += 1
            else:
                if cnt == 0:
                    res += s[i]
                else:
                    cnt -= 1
        return res[::-1]
