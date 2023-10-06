import sys,math
from typing import *

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        low,high=min(bloomDay),max(bloomDay)
        ans=high

        while low<=high:
            mid=(low+high)//2
            if (self.possible(bloomDay,mid,m,k)):
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans
    
    def possible(self,arr:List[int],day,m,k):
        no_of_bouquets=0
        cnt=0

        for i in range(len(arr)):
            if arr[i]<=day:
                cnt+=1
            else:
                no_of_bouquets+=(cnt//k)
                cnt=0
        no_of_bouquets+=cnt//k
        if no_of_bouquets>=m:
            return True
        return False

obj=Solution()
print(obj.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
print(obj.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))
print(obj.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))