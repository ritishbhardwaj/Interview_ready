from typing import *

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            missing=arr[mid]-(mid+1)

            if missing<k:
                low=mid+1
            else:
                high=mid-1
        
        return high+1+k
    
obj=Solution()
print(obj.findKthPositive(arr = [2,3,4,7,11], k = 5))
print(obj.findKthPositive(arr = [2,3,4,7,11], k = 6))
print(obj.findKthPositive(arr = [1,2,3,4], k = 2))


