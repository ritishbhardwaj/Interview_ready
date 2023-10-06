from typing import *
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        n=len(nums)

        #brute force
        l=1
        for i in range(n):
            maxi=mini=nums[i]
            for j in range(i+1,n):
            #getting mini & maxi of that particular subarray
                maxi=max(maxi,nums[j])
                mini=min(mini,nums[j])
                diff=abs(mini-maxi)

                if diff<=limit:
                    l=max(l,j-i)
                else:
                    break
        
        print(l+1)


        #optimised

        i=j=0
        l=1
        maxi=-float("inf")
        mini=float("inf")
        maxiInd=-1
        miniInd=-1

        while j<n:

            #calculations

            # maxi=max(maxi,nums[j])
            # mini=min(mini,nums[j])
            if nums[j]>=maxi:
                maxi=nums[j]
                maxiInd=j

            if nums[j]<=mini:
                mini=nums[j]
                miniInd=j
            # print(maxi,mini)

            diff=abs(maxi-mini)
            # print(diff,l)
            if diff<=limit:
                l=max(l,j-i+1)
                j+=1

            else:

                while i<n and diff>limit:
                    if nums[j]==maxi:
                        i=miniInd+1
                        miniInd=i
                        mini=nums[i]
                    elif nums[j]==mini:
                        i=maxiInd+1
                        maxiInd=i
                        maxi=nums[i]


                    diff=abs(maxi-mini)
                    # if diff

        print(l)
        print()




        

obj=Solution()
obj.longestSubarray(nums = [8,2,4,7], limit = 4)
obj.longestSubarray(nums = [10,1,2,4,7,2], limit = 5)
obj.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0)
obj.longestSubarray([2,2,2,4,4,2,5,5,5,5,5,2],2)
obj.longestSubarray([1,5,6,7,8,10,6,5,6],4)
obj.longestSubarray([7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87],63)