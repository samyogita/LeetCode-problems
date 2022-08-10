class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        if target in hashmap:
            return hashmap[target]
        else:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            
            
            