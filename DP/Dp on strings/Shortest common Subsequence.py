class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp,lengthOfLCS,i,j=self.longestCommonSubsequence(str1,str2)
        # print(dp)
        # print(i,j)
        supe=""
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                supe+=str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:   #up
                supe+=str1[i-1]
                i-=1
            else:              # left
                supe+=str2[j-1]
                j-=1
            
            # while i>0:
            #     supe+=str1[i-1]
            #     i-=1
            # while j>0:
            #     supe+=str2[j-1]
            #     j-=1                 
            ####################### AGAR MEI AISE LOOP RAKHTA HOO TO ANSWER MERA HOTA HAI BRUTEGROOT  :)

        while i>0:
                supe+=str1[i-1]
                i-=1
        while j>0:
            supe+=str2[j-1]
            j-=1

        print(supe[::-1],lengthOfLCS)
        return supe[::-1]    


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
                    ansB=0+max(dp[ind1-1][ind2],dp[ind1][ind2-1])
                    dp[ind1][ind2]=ansB
        
        return dp,dp[n][m],n,m

obj=Solution()
obj.shortestCommonSupersequence(str1 = "brute", str2 = "groot")
obj.shortestCommonSupersequence(str1 = "abac", str2 = "cab")
obj.shortestCommonSupersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa")