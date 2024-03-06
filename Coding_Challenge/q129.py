
class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        dp=[0]*(W+1)
        for i in range(N):
            for j in range(W+1):
                if j>=wt[i]:
                    dp[j]=max(dp[j],val[i]+dp[j-wt[i]])
        return dp[W]
        
