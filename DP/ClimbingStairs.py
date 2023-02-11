def sol(n,dp):
    if n<0: return 0
    if n==0:
        return 1
    
    if dp[n]!=None:
        return dp[n]

    left=sol(n-1,dp)
    right=sol(n-2,dp)

    res=left+right
    dp[n]=left+right

    return res



n=5
dp=[None]*(n+1)
ans=sol(n,dp)
print(ans)
