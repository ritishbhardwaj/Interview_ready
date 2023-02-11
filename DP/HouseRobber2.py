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
arr1=nums[0:len(nums)-1]
arr2=nums[1:]
print(arr1,arr2)
n1=len(arr1)
n2=len(arr2)
dp1=[None]*(n1+1)
ans1=sol(n1-1,arr1,dp1)
dp2=[None]*(n2+1)
ans2=sol(n2-1,arr2,dp2)
print(ans1)
print(ans2)
# return max(ans1,ans2)