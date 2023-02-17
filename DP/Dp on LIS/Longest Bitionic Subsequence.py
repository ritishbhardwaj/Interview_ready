from os import *
from sys import *
from collections import *
from math import *

def longestBitonicSequence(arr, n):
    # Write your code here.
    dp1=[1 for i in range(n)]
    dp2=[1 for i in range(n)]

    #to fill dp1
    for ind in range(1,n):
        for prev in range(ind):
            if arr[ind]>=arr[prev]:
                dp1[ind]=max(dp1[ind],dp1[prev]+1)

    #to fill dp2
    for ind in range(n-1,-1,-1):
        for prev in range(n-1,ind,-1):
            if arr[ind]>arr[prev]:
                dp2[ind]=max(dp2[ind],dp2[prev]+1)

    print(dp1)
    print(dp2)
    maxi=0
    for i in range(n):
        maxi=max(maxi,dp1[i]+dp2[i]-1)
    
    return maxi


ans=longestBitonicSequence([1,11,2,10,4,5,2,1],8)
# ans=longestBitonicSequence([1,2,1,2,1],5)
print(ans)