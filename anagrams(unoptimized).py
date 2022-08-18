class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = {}
        for i in strs:
            word = ''.join(sorted(i))
            if word not in arr:
                arr[word] = []
            arr[word].append(i)
        return arr.values()
        