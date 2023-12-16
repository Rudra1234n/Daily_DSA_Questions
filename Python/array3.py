class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        cur = 0
        maxsum = arr[0]
        
        for i in range(0,N):
            cur = cur + arr[i]
            if maxsum <cur :
                maxsum = cur
            if cur <0:
                cur = 0
        return maxsum
