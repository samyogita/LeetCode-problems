class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            rem = ((num - 1) % 9)+ 1
            return rem
        