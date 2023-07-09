# from collections import deque


class Solution:
    def solve(self,s,k):
        
        ##=============  recursion + memoisation =============
        dp=[-1]*(len(s)+1)
        return  self.actualSolveFunction(0,s,k,dp)


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


# print(int("110",base=2))
# print(bin(-2)[:])
# print(int("100"))

# def findMSB(n):
#     # Write your code here.
#     num=1
#     while True:
#         if num>n:
#             return num>>1
#         num=num<<1

# print(findMSB(22))\


from typing import List
# import heapq
# from collections import deque
# class Solution:
#     def minimumMagic(self, n : int, m : int, price : List[int], magical_price : List[int]) -> int:
#         # code here
#         # if sum(price)-sum(magical_price)>m:
#         #     return -1
#         if sum(price)<=m:
#             return 0
#         cnt=0
#         s=0
#         lower=[]
#         upper=[]
#         for i in range(n):
#             s+=magical_price[i]
#             lower.append(s)
#         s=0
#         for i in range(n-1,-1,-1):
#             s+=price[i]
#             upper.append(s)
#         upper.reverse()
#         for i in range(n-1):
#             totalsum=lower[i]+upper[i+1]
#             if totalsum<=m:
#                 return i+1
#         return -1
    
# obj=Solution()
# print(obj.minimumMagic(n = 5, m = 13 ,
# price = [3,4,6,2,4],magical_price = [1,2,5,1,3]))
# print(obj.minimumMagic(n = 3, m = 6, 
# price = [4,3,4]
# ,magical_price = [2,2,3]))
# print(obj.minimumMagic(4,21,[7,7,9,7],[6,3,3,3]))



    
obj=Solution()
print(obj.noOfPairs(box= ['bbcb', 'abccc', 'abc']))