from collections import *
from typing import *
from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # @cache
        def sol(ind,arr,target,dp):
            if target==0: 
                return True
            if ind==0: 
                return arr[0]==target
            
            if dp[ind][target]!=-1: return dp[ind][target]

            not_take=sol(ind-1,arr,target,dp)
            take=False
            if arr[ind]<=target:
                take=sol(ind-1,arr,target-arr[ind],dp)
            
            dp[ind][target]=not_take or take
            
            return not_take or take
        
        s=sum(nums)
        print(s)
        if s%2!=0: return False
        n=len(nums)
        target=s//2
        # dp=[[-1 for i in range(target+1)] for j in range(n)]
        # return sol(n-1,nums,target,dp)

        #======================= TABULATION ========================
        dp=[[0 for i in range(target+1)] for j in range(n)]
        for i in range(n):
            dp[i][0]=True
        if nums[0]<=target:
            dp[0][nums[0]]=True
        
        for i in range(n):
            for j in range(target+1):
                
                not_take=dp[i-1][j]
                take=False
                if nums[i]<=j:
                    take=dp[i-1][j-nums[i]]
                
                dp[i][j]=not_take or take
        # return dp[n-1][target]
        for i in dp:
            print(i)
        #====================Space Optimization =======================
        prev=[False for i in range(target+1)]
        # curr=[False for i in range(target+1)]
        prev[0]=True
        # curr[0]=True
        if nums[0]<=target:
            prev[nums[0]]=True
        for i in range(1,n):
            curr=[False for i in range(target+1)]
            # curr[0]=True
            for j in range(1,target+1):   
                not_take=prev[j]
                take=False
                if nums[i]<=j:
                    take=prev[j-nums[i]]
                
                curr[j]=not_take or take    
            prev=curr[:]
        print(prev,'-----------hh')
        return prev[target]    
                
obj=Solution()
nums = [1,5,11,5]
# nums = [100]
# nums = [1,2,3,5]
# nums = [1,2,5]
# nums =[97,99,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
print(obj.canPartition(nums=nums))