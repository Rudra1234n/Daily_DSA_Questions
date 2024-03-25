class Solution:
    def countWaystoDivide(self, n, k):
        # Code here
        if k>n:
            return 0
        def func(dp,ind,tar,k,n):
            if ind>n:
                return 0
            if ind==n and tar==0 and k==0:
                return 1
                
            if tar<0 or k<0:
                return 0
                
            if dp[ind][tar][k]!=-1:
                return dp[ind][tar][k]
                
            take=0
            
            if tar>=ind:
                take=func(dp,ind,tar-ind,k-1,n)
                
            nottake=func(dp,ind+1,tar,k,n)
            
            dp[ind][tar][k]=take+nottake
            return dp[ind][tar][k]
        
        dp=[[[-1 for i in range(n+1)] for j in range(n+1)] for k in range(n+1)]
        return func(dp,1,n,k,n)

