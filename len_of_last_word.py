class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        val = 0
        s = s.rstrip()
        for i in range(len(s)-1, -1,-1):
            if s[i] == ' ':
                break
            val += 1
        return val