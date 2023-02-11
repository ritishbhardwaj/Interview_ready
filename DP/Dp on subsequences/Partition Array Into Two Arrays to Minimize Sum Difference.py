from typing import *
import math
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
                
        def sol(ind,target,l,arr):
            
            if ind==0:
                if arr[0]==0: return True
                if target==0 or arr[0]==target: return True
                return False
            
            not_take=sol(ind-1,target,l,arr)
            take=False
            if arr[ind]<=target and l!=0:
                take=sol(ind-1,target-arr[ind],l-1,arr)
            
            return take or not_take
        
        n=len(nums)
        target = 13
        if n%2!=0: return False 
        l=n//2
        print(l)
        ans=sol(n-1,target,l,nums)
        return ans
        
        
obj=Solution()
# nums = [-36,36]
nums = [3,9,7,3]
ans=obj.minimumDifference(nums)
print(ans)


Not done yet