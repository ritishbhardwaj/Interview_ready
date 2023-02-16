from typing import *
class Solution:
    def PrintLIS(self, nums: List[int]) -> int:

        n=len(nums)
        dp=[1 for i in range(n)]
        hash=[None for i in range(n)]
        maxi=1
        lastIndex=0
        for ind in range(n):
            hash[ind]=ind
            for prev in range(ind):
                if nums[prev]<nums[ind]  and 1+dp[prev]>dp[ind]:
                    dp[ind]=1+dp[prev]
                    hash[ind]=prev

            if dp[ind]>maxi:
                maxi=dp[ind]
                lastIndex=ind
        print(dp,'-->',maxi,lastIndex)
        print(hash)
        print(lastIndex,'lastindex')
        print(maxi,'maxi')
        
        temp=[]
        temp.append(nums[lastIndex])

        while hash[lastIndex]!=lastIndex:
            lastIndex=hash[lastIndex]
            temp.append(nums[lastIndex])
        temp.reverse()
        print(temp)
obj=Solution()
# obj.PrintLIS([5,4,11,1,16,8])
obj.PrintLIS([1,2,4,8])