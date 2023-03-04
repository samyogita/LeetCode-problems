class Solution:
    def splitNum(self, num: int) -> int:
        num = str(num)
        nums = list(num)
        nums = sorted(nums)
        nums1 = ''
        nums2 = ''
        for i in range(len(nums)):
            if i % 2 == 0 or i == 0:
                nums1 += nums[i]
            else:
                nums2 += nums[i]
        return int(nums1)+int(nums2)
                
