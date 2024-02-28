class Solution:
    def factorial(self, N):
        #code here
        fact = 1
        if N==0:
            return [1]
        
        for i in range(N,0,-1):
            fact *= i
            
        lst = list(str(fact))

            
        return lst
