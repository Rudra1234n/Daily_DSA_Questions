class Solution:
    def countWays(self, n):
        
        dp = [0]*(n+1)
        
        
        if n >= 1:
            dp[1] = 1  # 1
        if n >= 2:
            dp[2] = 2  # 1+1, 2
        if n >= 3:
            dp[3] = 4  # 1+1+1, 2+1, 3, 3+1
        
        for i in range(4,n+1):
            x = dp[i-1]
            y = dp[i-2]
            z = dp[i-3]
            dp[i] = x+y+z
        
        return dp[n]%1000000007

