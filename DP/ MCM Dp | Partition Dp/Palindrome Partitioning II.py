from typing import *
import sys

class Solution:
    def minCut(self, s: str) -> int:
        
        n=len(s)

        def sol(ind,s,dp):
            if ind==n:
                return 0
            
            if dp[ind]!=-1:
                return dp[ind]
            temp=''
            mini=sys.maxsize

            for j in range(ind,n):
                temp+=s[j]
                if temp==temp[::-1]:
                    cost=1+sol(j+1,s,dp)
                    mini=min(cost,mini)
            dp[ind]=mini

            return mini

        dp=[-1]*(n)
        ans=sol(0,s,dp)
        print(ans-1)
        # return ans-1

        #=============TABULATION==========
        
        dp=[0]*(n+1)
        # temp=''
        # mini=sys.maxsize
        for ind in range(n-1,-1,-1):
            temp=''
            mini=sys.maxsize
            for j in range(ind,n):
                temp+=s[j]
                if temp==temp[::-1]:
                    cost=1+dp[j+1]
                    mini=min(cost,mini)
            dp[ind]=mini
        print(dp[0]-1)
        print()
        return dp[0]-1


obj=Solution()
obj.minCut('bababcbadcede')
obj.minCut('aab')
obj.minCut('a')
obj.minCut('ab')