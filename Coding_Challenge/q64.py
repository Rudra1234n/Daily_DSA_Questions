class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
        # code here 
        '''
        before low all ele will lower ele than a
        after high all ele will greater ele than b
        i will track ele that are in between a & b
        '''
        
        low = 0
        high = n-1
        
        i = 0
        while i <= high:
            if arr[i] < a:
                arr[low],arr[i] = arr[i], arr[low]
                low += 1
            elif arr[i] > b:
                arr[high],arr[i] = arr[i],arr[high]
                high -= 1
                i -= 1 # arr[high] get swapped at arr[i] and for arr[high] we do not checked
            i += 1
        return arr  
