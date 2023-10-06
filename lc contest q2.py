
from typing import *
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        i=len(nums)-2
        # print(sum(nums))
        s=nums[i+1]
        while i>=0:
            ele=nums[i]
            # grele=nums[i+1]
            if ele<=s:
                s=max(s,s+ele)
            else:
                s=nums[i]
            i-=1

        return s


obj=Solution()
print(obj.maxArrayValue(nums = [2,3,7,9,3]))
print(obj.maxArrayValue(nums = [2,3,7,9,1,2,4,2,5]))
print(obj.maxArrayValue(nums = [5,3,3]))