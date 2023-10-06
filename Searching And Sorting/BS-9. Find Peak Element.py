from typing import *
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #naive solution
        '''return nums.index(max(nums))'''

        #Optimal Solution
        low=0
        high=len(nums)-1
        if len(nums)==1:
            return 0
        if nums[1]<nums[0]:
            return 0
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1
        
        while low<=high:
            mid=(low+high)//2

            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            
            elif nums[mid]>nums[mid-1]:
                low=mid+1
            elif nums[mid] > nums[mid+1]:
                high=mid-1
            
            else:
                low=mid+1
            


obj=Solution()
print(obj.findPeakElement(nums = [1,2,1,3,5,6,4]))