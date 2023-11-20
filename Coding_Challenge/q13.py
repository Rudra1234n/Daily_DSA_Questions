class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        smallest = set(arr)
        for i in range(1, 100000):
            if i not in smallest:
                return i