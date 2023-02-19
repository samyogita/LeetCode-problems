
from sortedcontainers import SortedDict
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = SortedDict()
        arr = []
        for i in nums1:
            if i[0] in mp:
                mp[i[0]] += i[1]
            else:
                mp[i[0]] = i[1]
        for x in nums2:
            if x[0] in mp:
                mp[x[0]] += x[1]
            else:
                mp[x[0]] = x[1]
        print(mp)
        for i, j in mp.items():
            arr.append([i,j])
        return arr
            
                
