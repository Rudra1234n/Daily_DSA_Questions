class Solution:
    def isSubsetSum (self, N, arr, summ):
        # Minimum element of arr > summ
        if(min(arr)>summ):
            return False
        
        arr.sort()
        
        dp = [[False]*(summ+1) for i in range(N+1)]
        
        #Sum = 0 always possible
        for i in range(N+1):
            dp[i][0]=True
        
        for i in range(1, N+1):
            for j in range(1, summ+1):
                #j = sum excluding current element
                if(dp[i-1][j]==True):
                    dp[i][j]=True
                    
                #j = sum including current element
                if(j>=arr[i-1] and dp[i-1][j-arr[i-1]]==True):
                    dp[i][j]=True
        
        return dp[N][summ]

