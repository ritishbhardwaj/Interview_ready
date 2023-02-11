#========================Solution by me :) ===============
'''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count=0
        def sol(row,col,dp):
            nonlocal count
            if row==0 and col==0:
                # count+=1
                return 1
            if row<0 or col<0: 
                return 0

            if dp[row][col]!=-1: 
                # count+=1
                return dp[row][col]
            if row>=0:
                l=sol(row-1,col,dp)
            if col>=0:
                r=sol(row,col-1,dp)
            dp[row][col]=l+r
            return dp[row][col]
            
        dp=[[-1 for i in range(n)] for j in range(m)]
        ans=sol(m-1,n-1,dp)
        return ans

obj=Solution()
ans=obj.uniquePaths(m=4,n=5)
print(ans)'''

#=========================Solution Striver================
'''same hehe'''

# tabulation

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count=0
        def sol(row,col,dp):
            nonlocal count
            if row==0 and col==0:
                # count+=1
                return 1
            if row<0 or col<0: 
                return 0

            if dp[row][col]!=-1: 
                # count+=1
                return dp[row][col]
            if row>=0:
                l=sol(row-1,col,dp)
            if col>=0:
                r=sol(row,col-1,dp)
            dp[row][col]=l+r
            return dp[row][col]
            
        # dp=[[-1 for i in range(n)] for j in range(m)]
        # ans=sol(m-1,n-1,dp)
        # return ans
        #===============TABULATION===============
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    l,r=0,0
                    if i>0:
                        l=dp[i-1][j]
                    if j>0:
                        r=dp[i][j-1]
                    dp[i][j]=l+r
        # return dp[m-1][n-1]
        #===============TABULATION ENDS============
        
        #==============SPACE OPTIMIZATION ===============
        prev=[0 for i in range(n+1)]
        for i in range(m):
            curr=[0 for i in range(n)]
            for j in range(n):
                if i==0 and j==0:
                    curr[j] = 1
                else:
                    l,r=0,0
                    if i>0:
                        l=prev[j]
                    if j >0:
                        r=curr[j-1]
                    curr[j]=l+r
            prev=curr[:]
            
        return  prev[n-1],'space optimization'           
        


obj=Solution()
ans=obj.uniquePaths(m=4,n=5)
print(ans)
