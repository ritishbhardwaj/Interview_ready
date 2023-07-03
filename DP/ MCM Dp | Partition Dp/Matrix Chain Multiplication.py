from os import *
from sys import maxsize as mx
from collections import *
from math import *



def sol(i,j,arr,n,dp):
    if i==j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    minimum_score=mx*mx
    for partition in range(i,j):
        general_score=(arr[i-1]*arr[partition]*arr[j])+ sol(i,partition,arr,n,dp)+ sol(partition+1,j,arr,n,dp)
        minimum_score=min(minimum_score,general_score)
    dp[i][j]=minimum_score
    return minimum_score

    
def matrixMultiplication(arr,n):
    dp=[[-1 for i in range(n+1)] for j in range(n+1)]
    return sol(1,n-1,arr,n,dp) 
        



ans=matrixMultiplication([4,5,3,2],4)
print(ans)
ans=matrixMultiplication([40, 20, 30, 10, 30],5)
print(ans)