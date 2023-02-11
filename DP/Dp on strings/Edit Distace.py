class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n=len(word1)
        m=len(word2)
        

        #=========== 0 based indexing ===========
        def sol(s1,s2,i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            
            if dp[i][j]!=-1: return dp[i][j]

            if s1[i]==s2[j]:
                dp[i][j]=0+sol(s1,s2,i-1,j-1)
                return dp[i][j]

            insert=1+sol(s1,s2,i,j-1)
            delete=1+sol(s1,s2,i-1,j)
            replace=1+sol(s1,s2,i-1,j-1)

            ans=min(delete,insert,replace)
            dp[i][j]=ans
            return ans
        
        # dp=[[-1 for i in range(m+1)] for  j in range(n+1)]
        # ans=sol(word1,word2,n-1,m-1)
        # return ans

        #================= 1 based indexing ===============
        def sol(s1,s2,i,j,dp):
            if i==0:
                return j
            if j==0:
                return i 
            
            if dp[i][j]!=-1: return dp[i][j]

            if s1[i-1]==s2[j-1]:
                dp[i][j]=0+sol(s1,s2,i-1,j-1,dp)
                return dp[i][j]

            insert=1+sol(s1,s2,i,j-1,dp)
            delete=1+sol(s1,s2,i-1,j,dp)
            replace=1+sol(s1,s2,i-1,j-1,dp)

            ans=min(delete,insert,replace)
            dp[i][j]=ans
            return ans
        
        # dp=[[-1 for i in range(m+1)] for  j in range(n+1)]
        # ans=sol(word1,word2,n,m,dp)
        # return ans

        #================ TABULATION =============
        dp=[[0 for i in range(m+1)] for  j in range(n+1)]

        for j in range(m+1):
            dp[0][j]=j
        for i in range(1,n+1):
            dp[i][0]=i
        
        for i in range(1,n+1):
            for j in range(1,m+1):      # 1 se issliye bcoz j=0 ka hamne upar hi calculations kar lee hai
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=0+dp[i-1][j-1]
                    
                else: 
                    insert=1+dp[i][j-1]
                    delete=1+dp[i-1][j]
                    replace=1+dp[i-1][j-1]

                    ans=min(delete,insert,replace)
                    dp[i][j]=ans

        # return dp[n][m]

        #=============  SPACE OPTIMIZATION ===========
        curr=[0 for i in range(m+2)]
        prev=[0 for i in range(m+2)]

        for j in range(0,m+1):
            prev[j]=j
        
        for i in range(1,n+1):
            curr[0]=i
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    curr[j]=0+prev[j-1]
                else: 
                    insert=1+curr[j-1]
                    delete=1+prev[j]
                    replace=1+prev[j-1]

                    ans=min(delete,insert,replace)
                    curr[j]=ans
            prev=curr 

        print(prev)
        return prev[m]               



obj=Solution()
ans=obj.minDistance(word1 = "horse", word2 = "ros")
print(ans)
ans=obj.minDistance(word1 = "intention", word2 = "execution")
print(ans)