class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] <= 9:
                return digits
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
            else:
                digits[i-1] += 1
            
        return digits