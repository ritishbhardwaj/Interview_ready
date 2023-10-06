import sys,math
from typing import *
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low=1
        high=max(piles)
        ans=math.inf

        while low<=high:

            mid=(low+high)//2

            totalhours=sum([math.ceil(i/mid) for i in piles])
            # print(totalhours)
            if totalhours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans

obj=Solution()
print(obj.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(obj.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(obj.minEatingSpeed(piles = [30,11,23,4,20], h = 6))