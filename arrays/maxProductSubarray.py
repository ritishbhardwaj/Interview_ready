import math
from typing import *
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        p=1
        s=1
        maxi=-math.inf

        for i in range(len(nums)):

            # if p==0:                #[[[[ YE IF CONDITION KI POSITION KAHI BHI RAKH LO :) ]]]]
            #     p=1
            # if s==0:
            #     s=1

            p*=nums[i]
            maxi=max(maxi,p)
            s*=nums[len(nums)-1-i]
            maxi=max(s,maxi)


            if p==0:
                p=1
            if s==0:
                s=1

        return maxi

obj=Solution()
print(obj.maxProduct(nums = [2,3,-2,4]))
print(obj.maxProduct(nums = [-2,0,-1]))
print(obj.maxProduct([3,-6,4]))
