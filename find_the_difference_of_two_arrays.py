class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[i for i in set(nums1) if i not in nums2],[j for j in set(nums2) if j not in nums1]]
        return res
