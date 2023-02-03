class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = [0]
        for x in nums:
            pre.append(pre[-1]+x)

        for i in range(1, len(nums)):
            if pre[i-1] - pre[0] ==  pre[-1] - pre[i]:
                return i-1
        return -1