import math
from typing import *
import marshal
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def sol(ind,t,arr,dp):
            if ind==0:
                if t%arr[ind]==0: 
                    return t//arr[ind]
                return math.inf
            if dp[ind][t]!=-1: return dp[ind][t]
            not_take=0+sol(ind-1,t,arr,dp)
            take=math.inf
            if arr[ind]<=t:
                take=1+sol(ind,t-arr[ind],arr,dp)
            ans=min(not_take,take)
            dp[ind][t]=ans
            return ans
        
        n=len(coins)
        # dp=[[-1 for i in range(amount+1)] for j in range(n+1)]
        # ans=sol(n-1,amount,coins,dp)
        # if ans==math.inf:
        #     return -1
        # return ans

        #============== TABULATION ==============
        dp=[[0 for i in range(amount+1)] for j in range(n+1)]
        
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]= i//coins[0]
            else:
                dp[0][i]=math.inf
        
        for ind in range(1,n):
            for am in range(amount+1):
                
                not_take=0+dp[ind-1][am]
                take=math.inf
                if coins[ind]<=am:
                    take=1+dp[ind][am-coins[ind]]
                ans=min(take,not_take)
                dp[ind][am]=ans

        # return -1 if dp[n-1][amount]==math.inf else dp[n-1][amount]
    
        #===============  SPACE OPTIMIZATION ================
        prev=[0 for i in range(amount+1)]
        curr=[0 for i in range(amount+1)]
        for i in range(amount+1):
            if i%coins[0]==0:
                prev[i]= i//coins[0]
            else:
                prev[i]=math.inf
        
        for ind in range(1,n):
            for t in range(amount+1):
                
                not_take=0+prev[t]
                take=math.inf
                if coins[ind]<=t:
                    take=1+curr[t-coins[ind]]
                ans=min(take,not_take)
                curr[t]=ans
                print(curr,'',prev)
            prev=curr    
        print(curr,'  ',prev)        
        return -1 if prev[amount]==math.inf else prev[amount]
        
coins = [1,2,5]
amount = 11

# coins = [2]
# amount = 3

# coins = [1]
# amount = 0

obj=Solution()
ans=obj.coinChange(coins,amount)
print(ans)