class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums: List[int],l,r, target: int) -> int:
            while r >= l:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                return -1
            
        return binary_search(nums, 0, len(nums) - 1, target)