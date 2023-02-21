from os import *
from sys import *
from collections import *
from math import *

def matrixMultiplication(arr, n):
    dp=[[-1 for i in range(len(arr))] for j in range(len(arr))]
    return sol(1,len(arr)-1,arr,n,dp)
	
def sol(i,j,arr,n,dp):

    if i==j :
        return 0
    
    if dp[i][j]!=-1 : 
        return dp[i][j]
    mini=maxsize*maxsize
    for k in range(i,j):

        steps=(arr[i-1]*arr[k]*arr[j]) + sol(i,k,arr,n,dp)+sol(k+1,j,arr,n,dp)
        mini=min(mini,steps)
    dp[i][j]=mini

    return mini


ans=matrixMultiplication([4,5,3,2],4)
print(ans)