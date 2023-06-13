class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        text1=s[:]
        text2=s[::-1]
        print(text1,text2)
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
                    ansB=0+max(dp[ind1-1][ind2],dp[ind1][ind2-1])
                    dp[ind1][ind2]=ansB
        
        # print()
        print(dp[n][m])
        for i in dp:
            print(i)
        return dp[n][m]

        #============ SPACE OPTIMIZATION ==============
        # dp=[[0 for i in range(m+1)] for j in range(n+1)]
        prev=[0 for i in range(m+1)]
        curr=[0 for i in range(m+1)]
        for ind1 in range(n):
            for ind2 in range(m):

                if text1[ind1]==text2[ind2]:
                    ansA=1+prev[ind2-1]
                    curr[ind2]=ansA
                else:
                    ansB=0+max(prev[ind2],curr[ind2-1])
                    curr[ind2]=ansB
            prev=curr
        
        print(prev[m-1])
        return prev[m-1]

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
obj4.longestPalindromeSubseq('bbbab')
print()
obj4.longestPalindromeSubseq('cbbd')