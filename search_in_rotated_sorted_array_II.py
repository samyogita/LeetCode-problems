class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)==1:
            if nums[0]!=target:
                return False
            else:
                return True

        l=0
        r=len(nums)-1
        while(l<=r):

            while l<r and nums[l] == nums[l+1]:
                l+=1
            while l<r and nums[r] == nums[r-1]:
                r-=1

            mid=(l+r)//2
            if nums[mid]==target:
                return True

            elif nums[l]<=nums[mid]:
                if nums[mid]>=target and nums[l]<=target:
                    r=mid-1
                else:
                    l=mid+1

            else:
                if target>=nums[mid] and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False

