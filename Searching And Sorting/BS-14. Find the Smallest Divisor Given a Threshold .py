'''https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/'''

import math
from typing import *
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # for divisors  in range(1,max(nums)+1):
        #     if self.ans(nums,threshold,divisors):
        #         return divisors
        
        low,high=1,max(nums)
        ans=high
        while low<=high:
            mid=(low+high)//2

            if self.ans(nums,threshold,mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans,low
            
    def ans(self,arr:List[int],threshhold:int,divisor:int):
        total=0
        for i in range(len(arr)):
            total+= math.ceil(arr[i]/divisor)
        
        if total<=threshhold:
            return True
        return False

obj=Solution()
print(obj.smallestDivisor(nums = [1,2,5,9], threshold = 6))
print(obj.smallestDivisor(nums = [44,22,33,11,1], threshold = 5))