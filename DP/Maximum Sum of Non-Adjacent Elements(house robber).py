def sol(ind,arr,dp):
    if ind==0: return arr[ind]
    if ind<0: return 0
    if dp[ind]!=None: return dp[ind]
    pick =arr[ind]+sol(ind-2,arr,dp)
    notPick=0+sol(ind-1,arr,dp)

    res=max(pick,notPick)
    dp[ind]=res
    return res



nums = [2,7,3,1,9]
n=len(nums)
dp=[None]*(n+1)
ans=sol(n-1,nums,dp)
print(ans)