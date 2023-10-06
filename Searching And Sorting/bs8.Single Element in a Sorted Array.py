from typing import *
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        ele=-1
        if len(nums)==1:
            return nums[0]
        
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        
        while l<=h:
            mid=(l+h)//2
            
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]

            if (mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                l=mid+1
            
            else:
                h=mid-1
        
        return -1
    

obj=Solution()
print(obj.singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))
print(obj.singleNonDuplicate(nums = [3,3,7,7,10,11,11]))
print(obj.singleNonDuplicate([1,1,2,2,3,4,4,5,5,6,6]))