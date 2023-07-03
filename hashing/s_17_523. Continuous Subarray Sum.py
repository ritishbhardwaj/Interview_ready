from typing import *
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        check={0:-1}   # {rem : ind(first_occurance)}
        s=0
        ans=False
        for i in range(len(nums)):
            s+=nums[i]
            rem=s%k

            if rem in check:

                if i-check[rem]>=2:
                    return True
            else:
                check[rem]=i
        
        return ans
    
obj=Solution()
print(obj.checkSubarraySum(nums = [23,2,4,6,7], k = 6))
print(obj.checkSubarraySum( nums = [23,2,6,4,7], k = 6))