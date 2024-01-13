class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        
        m={}
        prefix=0
        for j,i in enumerate(arr):
            if i==0:
                return 1
                
            if prefix in m:
                return 1
                
            if prefix not in m:
                m[prefix]=j
                
            prefix+=i
            
        return 0
