from os import *
from sys import *
from collections import *
from math import *

from typing import List

def sol(ind,target,dp,arr):
    if target==0:
        return 1
    if ind==0:
        return arr[0]==target
    if dp[ind][target]!= -1: return dp[ind][target]
    not_taken=sol(ind-1,target,dp,arr)
    taken=0
    if arr[ind]<=target:
        taken=sol(ind-1,target-arr[ind],dp,arr)

    dp[ind][target]=taken+not_taken
    ans=taken+not_taken
    return ans

def findWays(num: List[int], tar: int) -> int:
    
    k=tar
    arr=num
    n=len(num)
    # dp=[[-1 for i in range(k+1)] for j in range(n)]
    # ans=sol(n-1,k,dp,arr)
    # if ans==False:
    #     return 0
    # if ans==True:
    #     return 1
    # return ans
    # dp=[[0 for i in range(k+1)] for j in range(n)]
    prev=[0 for i in  range(k+1)]
    prev[0]=1
    if arr[0]<=k:
        prev[arr[0]]=1
    curr=[0 for i in range(k+1)]
    curr[0]=1
    for ind in range(1,n):
        for target in range(1,k+1):
            not_take=prev[target]
            taken= 0
            if arr[ind]<=target:
                taken =prev[target-arr[ind]]
            curr[target]= not_take + taken
        prev=curr[:]
    return prev[k]


n=1
k=1
num=[0,0,1]
print(findWays(num,k))