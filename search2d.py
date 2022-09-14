class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searching(arr, target):
            l , r = 0, len(matrix[0]) - 1
            
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    r = mid - 1 
                else:
                    l = mid + 1
            return False
        
        if matrix == [] or matrix == [[]]:
            return False
        
        
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = l + (r - l) // 2
            val = searching(matrix[mid], target)
            if val == True:
                return True
            elif matrix[mid][-1] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            
                    
                    
            
        