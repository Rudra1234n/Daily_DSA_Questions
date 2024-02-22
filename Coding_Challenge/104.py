class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        for i in range(n):
            if i%2==1:
                if i-1>=0 and arr[i-1]>arr[i]:
                    arr[i-1],arr[i]=arr[i],arr[i-1]
                if i+1<n and arr[i+1]>arr[i]:
                    arr[i+1],arr[i]=arr[i],arr[i+1]
    
