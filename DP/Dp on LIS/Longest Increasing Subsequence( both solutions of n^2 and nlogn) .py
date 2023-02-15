from typing import *
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n=len(nums)

        #========MEMOIZATION================
        def sol(ind,prev,arr,dp):
            if ind==n:
                return 0
            
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            
            l=0+sol(ind+1,prev,arr,dp)
            if prev==-1 or arr[ind]>arr[prev]:
                l=max(l,1+sol(ind+1,ind,arr,dp))
            dp[ind][prev+1]=l
            return l

        dp=[[-1 for i in range(n+1)] for j in range(n)]
        ans=sol(0,-1,nums,dp)
        print(ans)
        # return ans

        #===========TABULATION============
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        
        for ind in range(n-1,-1,-1):
            for prev in range(ind-1,-2,-1):    # ind in recursion goes from -1 -> n-1 and here in TABULATION it goes from ind-1 to -1
                l=0+dp[ind+1][prev+1]   # here we did coordinates change beacuse whenever we take or store something in and from resp. from *DP TABLE* the prev should be [prev+1]
                if prev==-1 or nums[ind]>nums[prev]:  # here we didn't do prev+1 because **NUMS** is not **DP TABLE** and we are making coordinate shift on dp table only
                    l=max(l,1+dp[ind+1][ind+1])
                dp[ind][prev+1]=l
        print(dp[0][-1+1])
        # return dp[0][-1+1]

        #========== SPACE OPTIMIZATION =========
        next=[0 for i in range(n+2)]
        curr=[0 for i in range(n+2)]

        for ind in range(n-1,-1,-1):
            for prev in range(ind-1,-2,-1):    # ind in recursion goes from -1 -> n-1 and here in TABULATION it goes from ind-1 to -1
                l=0+next[prev+1]   # here we did coordinates change beacuse whenever we take or store something in and from resp. from *DP TABLE* the prev should be [prev+1]
                if prev==-1 or nums[ind]>nums[prev]:  # here we didn't do prev+1 because **NUMS** is not **DP TABLE** and we are making coordinate shift on dp table only
                    l=max(l,1+next[ind+1])
                curr[prev+1]=l
            next=curr

        print(next[-1+1])
        print(next,curr)
        print()
        return dp[0][-1+1]


obj=Solution()
obj.lengthOfLIS(nums = [10,9,2,5,3,7,101,18])
obj.lengthOfLIS(nums = [0,1,0,3,2,3])
obj.lengthOfLIS(nums = [7,7,7,7,7,7,7])
obj.lengthOfLIS([5,4,11,1,16,8])
