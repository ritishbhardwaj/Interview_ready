import sys
from typing import *
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        m=len(nums)
        nums.insert(0,1)
        nums.append(1)
        
        def sol(i,j,arr,dp):

            if i>j:
                return 0

            if dp[i][j]!=-1 :
                return dp[i][j]
            maxi=-sys.maxsize
            for ind in range(i,j+1):
                cost= (arr[i-1]*arr[ind]*arr[j+1])+sol(i,ind-1,arr,dp)+sol(ind+1,j,arr,dp)
                maxi=max(cost,maxi)
            dp[i][j]=maxi
            return maxi

        dp=[[-1 for i in range(m+1)] for j in range(m+1)]
        ans=sol(1,len(nums)-2,nums,dp)
        print(ans)
        return ans

obj=Solution()
obj.maxCoins( nums = [3,1,5,8])
obj.maxCoins(nums = [1,5])
