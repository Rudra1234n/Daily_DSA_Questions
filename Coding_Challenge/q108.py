class Solution:
    def segregateElements(self, arr, n):

        index=0 # index start with 0
        brr=arr.copy()  // make a copy of original array 
        
        for i in range (0,len(arr)):  # +ve array store 
            if (brr[i]>=0):
                arr[index]=brr[i]
                index+=1   # increment 
        for j in range (0,len (arr)):  # -ve array store 
            if (brr[j]<0):
                arr[index]=brr[j]
                index=index+1
