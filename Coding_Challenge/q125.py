class Solution:
    def LongestRepeatingSubsequence(self, str):
        n = len(str)
        i,j=0,0
        dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        def lcs(i,j):
            if(i==n or j==n):
                return 0
            take = 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            if(i!=j and str[i]==str[j]):
                take = 1+lcs(i+1,j+1)
            nt1 = lcs(i+1,j)
            nt2 = lcs(i,j+1)
            dp[i][j] =  max(nt1,nt2,take)
            return dp[i][j]
        return lcs(0,0)
