from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    
    dp=[[False for i in range(k+1)] for j in range(n)]
    # dp=[[-1 for i in range((10**3)+1)] for j in range((10**3)+1)]
    
    # ans=f(n-1,k,arr,dp)
    # return ans
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=k:
        dp[0][arr[0]]=True

    for ind in range(1,n):
        for target in range(1,k+1):
            not_take=dp[ind-1][target]
            taken= False
            if arr[ind]<=target:
                taken =dp[ind-1][target-arr[ind]]
            dp[ind][target]= not_take or taken
    # for i in dp:
    #     print(i)
    
    return dp[n-1][k]
    
def f(ind,target,arr,dp):
    if target==0:
        return True
    if ind==0:
        return target==arr[0]
    if dp[ind][target]!=-1: return dp[ind][target] 
    take=False
    if arr[ind]<=target:
        take=f(ind-1,target-arr[ind],arr,dp)    
    not_take=f(ind-1,target,arr,dp)

    dp[ind][target]=take or not_take

    return dp[ind][target]
    

n=4
k=299
arr=[97,99,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
print(subsetSumToK(n,k,arr))




# # A Dynamic Programming solution for subset
# # sum problem Returns true if there is a subset of
# # set[] with sun equal to given sum

# # Returns true if there is a subset of set[]
# # with sum equal to given sum
# def isSubsetSum(set, n, sum):
	
#     # The value of subset[i][j] will be
#     # true if there is a
#     # subset of set[0..j-1] with sum equal to i
#     subset =([[False for i in range(sum + 1)]
#             for i in range(n + 1)])

#     # If sum is 0, then answer is true
#     for i in range(n + 1):
#         subset[i][0] = True
        
#     # If sum is not 0 and set is empty,
#     # then answer is false
#     for i in range(1, sum + 1):
#         subset[0][i]= False
            
#     # Fill the subset table in bottom up manner
#     for i in range(1, n + 1):
#         for j in range(1, sum + 1):
#             if j<set[i-1]:
#                 subset[i][j] = subset[i-1][j]
#             if j>= set[i-1]:
#                 subset[i][j] = (subset[i-1][j] or
#                                 subset[i - 1][j-set[i-1]])

#     # uncomment this code to print table
#     for i in range(n + 1):
#         for j in range(sum + 1):
#             print (subset[i][j], end =" ")
#         print()
#     return subset[n][sum]
		
# # Driver code
# if __name__=='__main__':
# 	set = [3, 34, 4, 12, 5, 2]
# 	sum = 9
# 	n = len(set)
# 	if (isSubsetSum(set, n, sum) == True):
# 		print("Found a subset with given sum")
# 	else:
# 		print("No subset with given sum")