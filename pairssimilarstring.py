from collections import Counter
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        arr = [Counter(i) for i in words]
        print(arr)
        cnt = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if(arr[i].keys() == arr[j].keys()):
                    cnt += 1
        return cnt