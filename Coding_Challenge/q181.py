class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        def _lcs(x,y,s1,s2):
            if x == 0 or y == 0:
                return 0
            
            if dp[x-1][y-1]!=-1:
                return dp[x-1][y-1]

            if s1[x-1] == s2[y-1]:
                dp[x-1][y-1] = 1+ _lcs(x-1,y-1,s1,s2)
                return dp[x-1][y-1]
            
            dp[x-1][y-1] = max(_lcs(x-1,y,s1,s2),_lcs(x,y-1,s1,s2))
            return dp[x-1][y-1]
        dp = [[-1]*(y+1) for i in range(x+1)]
        
        res = _lcs(x,y,s1,s2)
        # print("DP",dp)
        return res
