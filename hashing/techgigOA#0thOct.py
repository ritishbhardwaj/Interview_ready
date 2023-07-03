


class Solution:
    def solve(self,s,k):
        
        ##=============  recursion + memoisation =============
        # dp=[-1]*(len(s)+1)
        # return  self.actualSolveFunction(0,s,k,dp)


        #  =======  Tabulation ==========

        dp=[0]*(len(s)+1)
        dp[len(s)]=1

        for ind in range(len(s)-1,-1,-1):
            ans=0
            for partition in range(ind,len(s)):
                substring_integer=(s[ind:partition+1])
                if int(substring_integer)<=k :
                    if len(substring_integer)>1 and substring_integer[0]=="0":
                        ans=ans+0
                        ####   or we can break the inner loop here
                    else:
                        ans=ans+dp[partition+1]

                else:
                    ans=ans+0
            dp[ind]=ans
        return dp[0]
    
    def actualSolveFunction(self,ind,string,k,dp):

        if ind==len(string):
            return 1
        
        if dp[ind]!=-1:
            return dp[ind]

        ans=0
        for partition in range(ind,len(string)):
            substring_integer=string[ind:partition+1]
            ref=int(string[ind:partition+1])
            if int(substring_integer)<=k :
                if len(substring_integer)>1 and substring_integer[0]=="0":
                    ans=ans+0
                else:
                    ans=ans+self.actualSolveFunction(partition+1,string,k,dp)

            else:
                ans=ans+0
        dp[ind]=ans
        return ans
    
obj=Solution()
print(obj.solve("120003",30))
print(obj.solve("123",1000))