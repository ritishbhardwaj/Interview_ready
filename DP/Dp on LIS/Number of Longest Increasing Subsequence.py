from typing import *
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1 for i in range(len(nums))]
        cnt=[1 for i in range(len(nums))]

        maxi=1
        for ind in range(1,n):
            for prev in range(ind):

                if nums[prev]<nums[ind] and 1+dp[prev]>dp[ind]:
                    dp[ind]=1+dp[prev]
                    cnt[ind]=cnt[prev]
                elif nums[prev]<nums[ind] and 1+dp[prev]==dp[ind]:
                    cnt[ind]+=cnt[prev]
            if dp[ind]>maxi:
                maxi=dp[ind]
        count=0
        for i in range(n):
            if dp[i]==maxi:
                count+=cnt[i]
        
        return count,dp,cnt

obj=Solution()
print(obj.findNumberOfLIS(nums = [1,3,5,4,7]))
print(obj.findNumberOfLIS(nums = [2,2,2,2,2]))
print(obj.findNumberOfLIS([2,2,2,2,2]))
print(obj.findNumberOfLIS([1,5,4,3,2,6,7,10]))