from typing import *
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        map={}
        cnt=0
        for i in range(len(nums)):
            cal1=nums[i]+k
            cal2=nums[i]-k
            
            
            if cal2 in map :
                cnt+=map[cal2]
            if cal1 in map:
                cnt+=map[cal1]            
            if nums[i] in map:
                map[nums[i]]+=1
            else:
                map[nums[i]]=1
            
        return cnt

obj=Solution()
# print(obj.countKDifference(nums = [1,2,2,1], k = 1))
# print(obj.countKDifference(nums = [1,3], k = 3))
# print(obj.countKDifference(nums = [3,2,1,5,4], k = 2))
print(obj.countKDifference([9,3,1,1,4,5,4,9,5,10],1))
