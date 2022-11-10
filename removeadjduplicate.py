class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = []
        for i in s:
            if not arr or arr[-1] != i:
                arr.append(i)
            else:
                arr.pop(-1)
        return ''.join(arr)
            