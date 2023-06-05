from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
             l=i+1
             r=len(nums)-1
             ele=nums[i]

             while l<r:

                if ele+nums[l]+nums[r]==0:
                    # pr/int(ele,nums[l],nums[r])
                    sarr=[ele,nums[l],nums[r]]
                    # print(sarr)
                    if sarr not in ans:
                        ans.append(sarr)
                    l+=1
                    r-=1
                if ele+nums[l]+nums[r]<0:
                    l+=1
                if ele+nums[l]+nums[r]>0:
                    r-=1
        # print(ans)
        return ans
                
obj=Solution()
print(obj.threeSum(nums = [-1,0,1,2,-1,-4]))
print(obj.threeSum(nums = [0,1,1]))
print(obj.threeSum(nums = [0,0,0]))