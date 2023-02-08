# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n 
        while r >= l:
            mid = l + (r-l) // 2
            if isBadVersion(mid) == False:
                l = mid + 1
            elif isBadVersion(mid) == True:
                r = mid - 1
                if isBadVersion(r) == False:
                    return r + 1
                else:
                    continue
