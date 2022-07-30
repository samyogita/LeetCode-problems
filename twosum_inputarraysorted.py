class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(numbers)):
            b = target - numbers[i]
            if b in pairs:
                return [pairs[b]+1, i+1]
            else:
                pairs[numbers[i]] = i