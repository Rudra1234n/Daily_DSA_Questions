class Solution:
    def insert(self, alist, index, n):
        #code here
        while index >= 0:
            if alist[index+1] < alist[index]:
                alist[index+1], alist[index] = alist[index], alist[index+1]
            index -= 1
            
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        if n == 1:
            return
        #code here
        for index in range(n-1):
            self.insert(alist, index, n)
