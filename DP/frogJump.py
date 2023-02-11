from datetime import time

from sys import maxsize
#=====================MEMOIZATION=================
def sol(ind,energy,dp):
    if ind==0: return 0

    if dp[ind] != None: return dp[ind]
    l=sol(ind-1,energy,dp)+ abs(energy[ind]-energy[ind-1])
    if ind>1:
        r=sol(ind-2,energy,dp)+ abs(energy[ind]-energy[ind-2])
    else:
        r=maxsize
    # print(maxsize)
    res=min(l,r)
    dp[ind]=res

    return res

h=[30,10,60,10,60,50,60,20,40]
n=len(h)
dp=[None]*(n+1)
print(sol(n-1,h,dp),'  <===Memoization')

#==================TABULATION===============
def sol2(arr,n,dp):
    dp[0]=0
    for i in range(1,n):
        fs=dp[i-1]+abs(arr[i]-arr[i-1])
        ss=maxsize
        if n>1:
            ss=dp[i-2]+abs(arr[i]-arr[i-2])

        res=min(fs,ss)
        dp[i]=res
    print(dp[n-1],end='')

dp1=[0]*(n+1)
sol2(h,n,dp1)
print('  <----Tabulation')

#======================Space optimized===========

def sol3(arr,n):
    prev,prev2=0,0
    for i in range(1,n):
        fs=prev+abs(arr[i]-arr[i-1])
        ss=maxsize
        if i>1:
            ss=prev2+abs(arr[i]-arr[i-2])
        cur=min(fs,ss)
        prev2=prev
        prev=cur
    print(cur,'   <======Space Optimized')

sol3(h,n)