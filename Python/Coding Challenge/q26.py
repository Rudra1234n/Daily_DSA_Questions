class Solution:
    def transitionPoint(self, arr, n): 
        if 1 in arr:
            return arr.index(1) 
        else:
            return -1
              
