from typing import *
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        for i in range(len(nums)-1-1,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            nums.sort()
            print(nums)
            return nums
        
        for i in range(len(nums)-1,ind-1,-1):
            if nums[i]>nums[ind]:
                temp=nums[i]
                nums[i]=nums[ind]
                nums[ind]=temp
                break
        nums[ind+1:]=sorted(nums[ind+1:])

        print(nums)
        return nums
        


obj=Solution()

obj.nextPermutation(nums = [1,2,3])
obj.nextPermutation(nums = [1,1,5])
obj.nextPermutation([3,2,1])
obj.nextPermutation([2,1,5,4,3,0,0])