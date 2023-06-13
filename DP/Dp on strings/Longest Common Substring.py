class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        #==============TABULATION ===============
        dp=[[0 for i in range(m+1)] for j in range(n+1)]

        for ind2 in range(m+1): dp[0][ind2]=0
        for ind1 in range(n+1): dp[ind1][0]=0

        for ind1 in range(1,n+1):     # because of 1 based indexing after shifting of indeces thereby range of n is n,n-1,n-1,......,1
            for ind2 in range(1,m+1):

                if text1[ind1-1]==text2[ind2-1]:
                    # print(text1[ind1-1],end='')
                    ansA=1+dp[ind1-1][ind2-1]
                    dp[ind1][ind2]=ansA
                else:
                    ansB=0
                    dp[ind1][ind2]=ansB
        
        # print()
        maxi=-float('inf')
        for i in dp:
            print(i)
            maxi=max(maxi,max(i))
        print(maxi)
        return maxi


# obj=Solution()
# obj.longestCommonSubsequence(text1 = "abc", text2 = "def")
# print()
# obj2=Solution()
# obj2.longestCommonSubsequence(text1 ="ezupkr", text2 ="ubmrapg")
# print()
# obj3=Solution()
# obj3.longestCommonSubsequence(text1 = "abghiimfnc", text2 = "abghqwppwc")
# print()
obj4=Solution()
obj4.longestCommonSubsequence(text1='abcde',text2='bccdgek')