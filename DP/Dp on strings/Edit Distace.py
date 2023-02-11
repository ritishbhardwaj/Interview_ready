class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n=len(word1)
        m=len(word2)
        
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
        
        dp=[[-1 for i in range(m+1)] for  j in range(n+1)]
        ans=sol(word1,word2,n-1,m-1)
        return ans

obj=Solution()
ans=obj.minDistance(word1 = "horse", word2 = "ros")
print(ans)
ans=obj.minDistance(word1 = "intention", word2 = "execution")
print(ans)