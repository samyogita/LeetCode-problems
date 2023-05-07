class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        arr = []
        for i in range(len(obstacles)):
            ans = bisect_right(arr,obstacles[i])
            if ans == len(arr):
                arr.append(obstacles[i])
                
            else:
                arr[ans] = obstacles[i]
            res.append(ans+1)
        return res
            
