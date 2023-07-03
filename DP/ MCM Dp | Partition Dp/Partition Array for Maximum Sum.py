import sys
from typing import *

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        n=len(arr)

        def sol(ind,arr,k,dp):
            if ind==n:
                return 0
            if dp[ind]!=-1 :
                return dp[ind]
                
            l=0  # to calculate the length of subarray
            maxAns=-sys.maxsize
            maxi=-sys.maxsize  # to calculate the maximum element in that particular subarray

            for j in range(ind,min(n,ind+k)):
                l+=1
                maxi=max(arr[j],maxi)
                summ=(l*maxi)+sol(j+1,arr,k,dp)
                maxAns=max(maxAns,summ)
            dp[ind]=maxAns
            return maxAns

        dp=[-1]*(n+1)
        ans=sol(0,arr,k,dp)
        print(ans)
        return ans



obj=Solution()
obj.maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3)
obj.maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4)
obj.maxSumAfterPartitioning(arr =[20779,436849,274670,543359,569973,280711,252931,424084,361618,430777,136519,749292,933277,477067,502755,695743,413274,168693,368216,677201,198089,927218,633399,427645,317246,403380,908594,854847,157024,719715,336407,933488,599856,948361,765131,335089,522119,403981,866323,519161,109154,349141,764950,558613,692211],k =26)
