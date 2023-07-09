


class Solution:
    def solve(self,arr):
        

        #======= to calculate odd paths
        def f(ind,s,arr,dp):
            if ind==len(arr)-1:
                if (s+arr[ind])%2!=0:
                    return 1
                return 0
            if ind>len(arr)-1:
                return 0
            
            if (ind,s) in dp:
                return dp[(ind,s)]
            step1=f(ind+1,s+arr[ind],arr,dp)
            step2=f(ind+2,s+arr[ind],arr,dp)
            step3=f(ind+3,s+arr[ind],arr,dp)
            dp[(ind,s)]=step1+step2+step3
            return step1+step2+step3
        
        #====== to calculate even paths
        def f1(ind,s,arr,dp):
            if ind==len(arr)-1:
                if (s+arr[ind])%2==0:
                    return 1
                return 0
            if ind>len(arr)-1:
                return 0
            
            if (ind,s) in dp:
                return dp[(ind,s)]
            step1=f1(ind+1,s+arr[ind],arr,dp)
            step2=f1(ind+2,s+arr[ind],arr,dp)
            step3=f1(ind+3,s+arr[ind],arr,dp)
            dp[(ind,s)]=step1+step2+step3
            return step1+step2+step3

        dp={}
        ans=f(0,0,arr,dp)
        print(dp)
        dp={}
        ans2=f1(0,0,arr,dp)
        print()
        print(dp)
        print()
        return ans+ans2

obj=Solution()
print(obj.solve([5,4,2,6,8]))
print()
print(obj.solve([2 ,3, 5, 8 ,10 ]))
print()
print(obj.solve([1,6,6,9,7,3,9,5,4,1,2,3,6,5]))
print()
