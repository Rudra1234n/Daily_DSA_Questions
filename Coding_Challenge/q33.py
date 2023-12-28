
class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        arr=[0]*(n+m)
        for i in range(n):
            arr[i]=arr1[i]
        for i in range(m):
            arr[i+n]=arr2[i]
        arr.sort()
        for i in range(n):
            arr1[i]=arr[i]
        for i in range(m):
            arr2[i]=arr[i+n]
    
