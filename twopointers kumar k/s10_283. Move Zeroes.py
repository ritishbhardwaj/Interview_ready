from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i=j=0
        while j<len(nums) and i<len(nums):
            if i==j:
                j+=1
                continue
            
            if nums[i]==0 and nums[j]!=0:
                nums[i]=nums[j]
                nums[j]=0
                j+=1
                i+=1
            
            # elif nums[i]==0 and nums[j]==0:
            #     j+=1
            #     # i+=1
            # elif nums[i]
            else:
                j+=
        
        return nums

obj=Solution()
print(obj.moveZeroes([0,1,0,3,12]))
print(obj.moveZeroes([1,0,3,6,5,0,3,0,4,0,0,6,9,8,3,7,0,0,3,4,1,2,5,6,99,2,1,4,0]))