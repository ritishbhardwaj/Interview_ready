class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(p)
        m=len(s)

        #========== 0 based indexing===============

        def sol(s1,s2,i,j,dp):       #s1 shows pattern      s2 shows input string
            #BASE CASE            
            if i<0 and j<0:
                return True
            if i<0 and j>=0:
                return False
            if j<0 and i>=0:
                for ii in range(i+1):
                    if s1[ii] != '*':
                        return False
                return True

            if dp[i][j]!=-1 : 
                return dp[i][j]

            #Matching condition
            if s1[i]==s2[j] or s1[i]=='?':
                ansA= sol(s1,s2,i-1,j-1,dp)
                dp[i][j]=ansA
                return ansA
            
            #Not matching condition
            if s1[i]=='*':
                ansB= sol(s1,s2,i-1,j,dp) or sol(s1,s2,i,j-1,dp)
                dp[i][j]=ansB
                return ansB

            if s1[i]!=s2[j]:
                dp[i][j]=False
                return False
        
        # dp=[[-1 for i in range(m+1)] for j in range(n+1) ]
        # ans=sol(p,s,n-1,m-1,dp)
        # print(ans)
        # return ans
        
        #========= 1 based indexing ===========
        def sol(s1,s2,i,j,dp):       #s1 shows pattern      s2 shows input string
            #BASE CASE            
            if i==0 and j==0:
                return True
            if i==0 and j>=1:
                return False
            if j==0 and i>=1:
                # for ii in range(i):
                    # if s1[ii] != '*':
                    #     return False
                for ii in range(1,i):
                    if s1[ii-1] != '*':
                        return False
                return True

            if dp[i][j]!=-1 : 
                return dp[i][j]

            #Matching condition
            if s1[i-1]==s2[j-1] or s1[i-1]=='?':
                ansA= sol(s1,s2,i-1,j-1,dp)
                dp[i][j]=ansA
                return ansA
            
            #Not matching condition
            if s1[i-1]=='*':
                ansB= sol(s1,s2,i-1,j,dp) or sol(s1,s2,i,j-1,dp)
                dp[i][j]=ansB
                return ansB

            if s1[i-1]!=s2[j-1]:
                dp[i][j]=False
                return False


        # dp=[[-1 for i in range(m+1)] for j in range(n+1) ]
        # ans=sol(p,s,n,m,dp)
        # print(ans)
        # return ans

        #============ TABULATION =============
        s1=p[:]
        s2=s[:]
        dp=[[False for i in range(m+1)] for j in range(n+1) ]

        dp[0][0]=True

        for j in range(1,m+1):
            dp[0][j]=False

obj=Solution()
obj.isMatch(s = "aa", p = "a")
obj.isMatch(s = "aa", p = "*")
obj.isMatch(s = "cb", p = "?a")
obj.isMatch(s = "abdefcd", p = "ab*cd")