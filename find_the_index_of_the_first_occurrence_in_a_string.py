class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            found = haystack[i:i+len(needle)]
            if found == needle:
                return i
            elif len(found) >= len(haystack):
                break
        return -1
