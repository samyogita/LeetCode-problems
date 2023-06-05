class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x = (x2-x1)
        y = (y2-y1)
        for i in range(1, len(coordinates)-1):
            cur_x1, cur_y1 = coordinates[i]
            cur_x2,cur_y2 = coordinates[i+1]
            if y *((cur_x2-cur_x1)) != x*((cur_y2-cur_y1)):
                return False
        return True
