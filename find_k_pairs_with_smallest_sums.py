from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        vis = set()
        pq = [(nums1[0]+nums2[0],(0,0))]
        vis.add((0,0))
        cnt = 0
        while k > 0 and pq:
            total, (i,j) = heappop(pq)
            ans.append((nums1[i],nums2[j]))

            if i+1 < len(nums1) and (i+1, j) not in vis:
                heappush(pq, (nums1[i+1]+nums2[j],(i+1,j)))
                vis.add((i+1,j))
            
            if j+1 < len(nums2) and (i, j+1) not in vis:
                heappush(pq, (nums1[i]+nums2[j+1],(i,j+1)))
                vis.add((i,j+1))
            
            k -= 1
        return ans
