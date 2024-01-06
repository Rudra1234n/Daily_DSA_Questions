class Solution:
	def editDistance(self, s, t):
        # Code here
        ns = len(s)
        nt = len(t)
        
        dp = [[0 for i in range(nt+1)] for i in range (ns+1)]
        
        for i in range(ns+1):
            for j in range(nt+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    a = dp[i-1][j-1] + 1
                    b = dp[i][j-1] + 1
                    c = dp[i-1][j] + 1
                    
                    val = min(a, min(b, c))
                    
                    dp[i][j] = val
        
        return dp[ns][nt]

