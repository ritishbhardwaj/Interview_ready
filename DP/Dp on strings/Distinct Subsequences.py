class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        n=len(s)
        m=len(t)

        #======== Memo with 0 based indexing ===========
        def sol(i,j,s1,s2,dp):
            if j<0:
                return 1
            if i<0:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if s1[i]==s2[j]:
                take=sol(i-1,j-1,s1,s2,dp)
                not_take=sol(i-1,j,s1,s2,dp)
                dp[i][j]=take+not_take
                return dp[i][j]
            else:
                not_take=sol(i-1,j,s1,s2,dp)
                dp[i][j]=not_take
                return not_take

        # dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        # return sol(n-1,m-1,s,t,dp)
        #============= Memo with 1 based indexing ===============
        def sol(i,j,s1,s2,dp):
            if j==0:
                return 1
            if i==0:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if s1[i-1]==s2[j-1]:
                take=sol(i-1,j-1,s1,s2,dp)
                not_take=sol(i-1,j,s1,s2,dp)
                dp[i][j]=take+not_take
                return dp[i][j]
            else:
                not_take=sol(i-1,j,s1,s2,dp)
                dp[i][j]=not_take
                return not_take

        # dp=[[-1 for i in range(m+1)] for j in range(n+1)]                
        # return sol(n,m,s,t,dp)

        #============ TABULATION ============
        s1=s[:]
        s2=t[:]
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for j in range(1,m+1):
            dp[0][j]=0

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    take=dp[i-1][j-1]
                    not_take=dp[i-1][j]
                    dp[i][j]=take+not_take
 
                else:
                    not_take=dp[i-1][j]
                    dp[i][j]=not_take

        # for i in dp:
        #     print(i)
        # return dp[n][m]

        #============ Space Optimization ==============
        prev=[0 for i in range(m+1)]
        curr=[0 for j in range(m+1)]

        prev[0],curr[0]=1,1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    take= prev[j-1]
                    not_take= prev[j]
                    prev[j]=take+not_take
 
                else:
                    not_take=prev[j]
                    prev[j]=not_take
            # prev=curr
        print(prev,curr)
        return prev[m]


obj=Solution()
ans=obj.numDistinct(s = "babgbag", t = "bag")
print(ans)

ans=obj.numDistinct(s = "rabbbit", t = "rabbit")
print(ans)

ans=obj.numDistinct(s='b',t='b')
print(ans)