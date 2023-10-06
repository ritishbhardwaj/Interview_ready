import math,sys
from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        mini=math.inf
        # print(mini)
        while l<=h:
            mid=(l+h)//2

            #left sorted
            if nums[mid]>=nums[l]:
                mini=min(mini,nums[l])
                l=mid+1
            else:
                mini=min(nums[mid],mini)
                h=mid-1
        
        return mini

obj=Solution()
print(obj.findMin(nums = [3,4,5,1,2]))
print(obj.findMin(nums = [4,5,6,7,0,1,2]))
print(obj.findMin(nums = [11,13,15,17]))
print(obj.findMin([2]))