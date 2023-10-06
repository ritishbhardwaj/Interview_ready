from math import *
def floorSqrt(n):

    low,high=1,n
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid**2<=n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return high,ans,low

print(floorSqrt(15))