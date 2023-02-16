from typing import *
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()   # [1,2,4,7,8,14,16]
        dp=[1 for i in range(len(nums))]
        temp=[]
        maxi=1
        lastIndex=0
        hash=[0 for i in range(len(nums))]
        for ind in range(1,len(nums)):
            hash[ind]=ind
            for prev in range(0,ind):
                a=nums[ind]
                b=nums[prev]
                if nums[ind]%nums[prev]==0 and dp[prev]+1 > dp[ind]:
                    hash[ind]=prev
                    dp[ind]=dp[prev]+1
            
            if dp[ind]>maxi:
                maxi=dp[ind]
                lastIndex=ind

        print(dp)
        temp.append(nums[lastIndex])

        while hash[lastIndex]!=lastIndex:
            lastIndex=hash[lastIndex]
            temp.append(nums[lastIndex])
        temp.reverse()
        print(temp)



obj=Solution()
obj.largestDivisibleSubset([1,2,4,8])