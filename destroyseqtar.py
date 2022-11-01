from sortedcontainers import SortedList
import math
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mp = defaultdict(SortedList)
        for i in range (len(nums)):
            n = nums[i] % space
            mp[n].add(nums[i]) 
        arr = []
        for key in mp:
            arr.append(len(mp[key]))  
        mx = max(arr)
        mn = math.inf
        for keys, values in mp.items():
            if mx == len(values) and mp[keys][0] < mn:
                mn = values[0]
        return mn
                