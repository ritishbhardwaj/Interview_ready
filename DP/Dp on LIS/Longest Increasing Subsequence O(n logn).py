import bisect
from typing import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        temp=[]
        l=1
        temp.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
                l+=1
            else:
                # ind=bisect.bisect_right(temp,nums[i])
                ind=bisect.bisect_left(temp,nums[i])
                # print(ind)
                print(ind,temp)
                temp[ind]=nums[i]
        print(temp)
        print(l)
        return l

obj=Solution()
# obj.lengthOfLIS(nums = [1,7,8,4,5,6,-1,9])
# obj.lengthOfLIS([1,4,5,4,2,8])
obj.lengthOfLIS([1,7,7,7,7,7,7,7])
