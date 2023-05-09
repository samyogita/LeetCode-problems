from collections import defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = [0]
        vis = set()
        levels = 0
        mp = defaultdict(list)
        for j,i in enumerate(arr):
            mp[i].append(j)
        while q:
            found = False
            nq = []
            for x in q:
                if x == len(arr)-1:
                    found = True
                    break
                vis.add(x)
                if x-1 >= 0 and x-1 not in vis:
                    nq.append(x-1)
                if x+1 < len(arr) and x+1 not in vis:
                    nq.append(x+1)
                for i in mp[arr[x]]:
                    if i not in vis:
                        nq.append(i)
                mp.pop(arr[x])
            if found:
                break
            levels += 1
            
            q = nq
        return levels

                
                


