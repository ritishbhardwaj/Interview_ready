from collections import *
from typing import * 
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        
        # mapp=defaultdict(int)
        # for i in range(len(usageLimits)):
        #     mapp[i]=usageLimits[i]

        # usageLimits.sort()
        c=Counter(usageLimits)
        cnt=0
        arr=sorted(set(usageLimits))
        if len(arr)==1:
            ele=arr[0]
            if ele>=len(usageLimits):
                return len(usageLimits)
            elif c[ele]<=len(usageLimits):
                return ele
            else:
                return ele+1
        else:
            pass
        



obj=Solution()
ans=obj.maxIncreasingGroups(usageLimits = [1,2,5])
print(ans)
ans=obj.maxIncreasingGroups([3,3,3,3])
print(ans)

ans=obj.maxIncreasingGroups([1,1])
print(ans)