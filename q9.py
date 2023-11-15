#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr, n):
        # code here
        dp=[[[0,0],[0,0]] for i in range(n)]
        dp[n-1]=[[arr[n-1],arr[n-1]],[arr[n-1],arr[n-1]]]
        for i in range(n-2,-1,-1):
            if(arr[i]<0):
                dp[i][0][0]=max(arr[i]*dp[i+1][1][1],dp[i+1][0][0],arr[i])
                dp[i][1][0]=max(arr[i],arr[i]*dp[i+1][1][1])
                dp[i][1][1]=min(arr[i],arr[i]*dp[i+1][1][0])
            else:
                dp[i][0][0]=max(arr[i]*dp[i+1][1][0],arr[i],dp[i+1][0][0])
                dp[i][1][0]=max(arr[i],arr[i]*dp[i+1][1][0])
                dp[i][1][1]=min(arr[i],arr[i]*dp[i+1][1][1])
        return dp[0][0][0]