from typing import *
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    def sol(n,arr,dp,last,ind,tasks):
        if ind==0:
            maxi=0
            for i in range(tasks):
                if i != last:
                    maxi=max(maxi,arr[0][i])
            return maxi
        maxi=0
        if dp[ind][last]!=-1: return dp[ind][last]
        for i in range(tasks):
            if i!=last:
                tt=arr[ind][i]+sol(n,arr,dp,i,ind-1,tasks)
                maxi=max(maxi,tt)
        dp[ind][last]=maxi        
        return maxi

    dp=[[-1 for j in range(4)] for i in range(n) ]
    days=len(points)-1
    last=3
    tasks=len(points[0])
    ans=sol(n,points,dp,last,days,tasks)
    return ans


n=3
# points=[[1,2,5,6,7,2,3,6,9],[3,1,1,8,6,4,2,3,8],[3,3,3,4,8,5,3,6,2],[1,2,5,6,7,2,3,6,9],[1,2,5,9,7,2,3,6,9],[1,2,5,6,7,5,3,6,11]]
points=[[10 ,40, 70],[20, 50, 80],[30, 60, 90]]
# print(dp)
print(ninjaTraining(n,points))