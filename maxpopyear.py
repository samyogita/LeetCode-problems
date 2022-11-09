class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0] * 2051
        for ele in logs:
            l = ele[0]
            r = ele[1]
            arr[l] += 1
            arr[r] -= 1
        for i in range(1, 2051):
            arr[i] += arr[i-1]
        mx = 0
        year = 1950
        for i in range(1950, 2051):
            if arr[i] > mx:
                mx = arr[i]
                year = i
        return year