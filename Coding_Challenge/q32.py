class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        a = []
        b = []
        c = k-1
        for i in range(n-c):
            for j in range(i,k+i):
                a.append(arr[j])
            Max = max(a)
            b.append(Max)
            a.clear()
        return b       