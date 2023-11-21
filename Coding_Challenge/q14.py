class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        for i in range(n):
            l=i+1
            r=n-1
            remain=-arr[i]
            while l<r:
                if arr[l]+arr[r]<remain:
                    l+=1
                elif arr[l]+arr[r]>remain:
                    r-=1
                else:
                    return 1