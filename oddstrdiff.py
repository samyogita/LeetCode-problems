class Solution:
    def oddString(self, words: List[str]) -> str:
        mp = {}
        for i in words:
            arr = []
            for j in range(1, len(i)):
                diff = ord(i[j]) - ord(i[j-1])
                arr.append(diff)
            ans = tuple(arr)
            if ans not in mp:
                mp[ans] = []
            mp[ans].append(i)
            
        for key in mp:
            if len(mp[key]) == 1:
                res = mp[key]
                return res[0]
                
                