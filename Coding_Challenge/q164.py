class Solution:
    def leftRotate(self, arr, n, d):
        
        # first reverse the array from 0 to d-1
        l, r = 0, d-1
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1 
            r-=1 
            
        # reverse the array from d to len(arr)-1
        l, r = d, len(arr)-1
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
            
        # reverse the entire array 
        l, r = 0, len(arr)-1
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
            
        return arr 
