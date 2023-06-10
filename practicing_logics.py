
from bisect import bisect_left,bisect_right


def bs(arr,t):
    l=0
    r=len(arr)-1
    ans=bisect_left(arr,4)
    ans=bisect_right(arr,4)
    print(ans)


arr=[1,2,3,4,5]
t=2
bs(arr,t)