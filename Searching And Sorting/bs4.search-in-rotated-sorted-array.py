
from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Brute force O(n)
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        


        low=0
        high=len(nums)-1

        
        while low<=high:

            mid=(low+high)//2

            if nums[mid]==target:
                return mid
            
            # left is sorted
            if nums[mid]>=nums[low]:
                if nums[mid]>=target and nums[low]<=target:
                    high-=1
                else:
                    low+=1
            
            # right is sorted
            else:
                if target>=nums[mid] and nums[high]>=target:
                    low+=1
                
                else:
                    high-=1

        return -1

obj=Solution()
print(obj.search(nums = [4,5,6,7,0,1,2], target = 0))
print(obj.search(nums = [4,5,6,7,0,1,2], target = 3))
print(obj.search(nums = [1], target = 0))