class Solution:
    def minimumSum(self, num: int) -> int:
        numbers = []
        num = str(num)
        for i in range(4):
            numbers.append(num[i])
        numbers.sort()
        new1 = str(numbers[0] + numbers[2])
        new2 = str(numbers[1] + numbers[3])
        
        return (int(new1)+int(new2))