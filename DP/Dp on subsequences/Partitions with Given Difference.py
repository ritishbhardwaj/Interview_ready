class Solution:
    def countPartitions(self, n, d, arr):
        mod=(10**9)+7
        s=sum(arr)
        if s-d<0 or (s-d)%2!=0: return 0
        k= (s-d)//2        #k is denoted as target 
        dp=[[-1 for i in range(k+1)] for j in range(n)]
        ans=self.sol(n-1,k,dp,arr)
        # print(ans)
        if ans==False:
            return 0
        if ans==True:
            return 1
        # return ans % (10**9)+7
        
        dp=[[0 for i in range(k+1)] for j in range(n+1)]

        prev=[0 for i in range(k+1)]
        curr=[0 for i in range(k+1)]
        if arr[0]==0 : 
            prev[0]=2
        else:
            prev[0]=1
        if arr[0]<=k and arr[0]!=0:
            prev[arr[0]]=1
        for ind in range(1,n):
            for target in range(k+1):
                not_taken=prev[target]
                taken =0
                if arr[ind]<=target: 
                    taken=prev[target-arr[ind]] 
                curr[target]=taken +not_taken
            prev=curr[:]    
                
        return prev[k] % mod
        
            
    def sol(self,ind,target,dp,arr):
        if ind==0:
            if target==0 and arr[0]==0: 
                return 2
            if target==0 or arr[0]==target : return 1
            return 0
        
        if dp[ind][target]!= -1: 
            return dp[ind][target]
        
        not_taken=self.sol(ind-1,target,dp,arr)
        taken=0
        if arr[ind]<=target:
            taken=self.sol(ind-1,target-arr[ind],dp,arr)

        dp[ind][target]=taken+not_taken
        ans=taken+not_taken
        return ans
        
    
obj=Solution()
n = 4
d = 0
arr =  [1,1,1,1]
print(obj.countPartitions(n,d,arr)