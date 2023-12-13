class Solution:
    
    #Function to find maximum of each subarray of size k.


    def max_of_subarrays(self,arr,N,K):
        result = []
        dq = []
    
        # Process the first window separately
        for i in range(K):
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
    
        # Process the remaining windows
        for i in range(K, N):
            result.append(arr[dq[0]])
    
            # Remove elements outside the current window
            while dq and dq[0] <= i - K:
                dq.pop(0)
    
            # Remove elements smaller than the current element from the back
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
    
            dq.append(i)
    
        # Add the maximum of the last window
        result.append(arr[dq[0]])
    
        return result    