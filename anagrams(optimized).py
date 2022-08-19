class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = {}
        for i in strs:
            mp = [0] * 26
            for j in i:
                pos = ord(j) - ord('a')
                mp[pos] +=1
            ans = tuple(mp)
            if ans not in arr:
                arr[ans] = []
            arr[ans].append(i)
        
        return arr.values()
                
                
        