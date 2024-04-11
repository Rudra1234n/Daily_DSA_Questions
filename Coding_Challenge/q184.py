class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    def fractionalknapsack(self, W,arr,n):
        arr.sort(key=lambda x : x.weight/x.value)
        i = 0
        profit = 0
        
        while W > 0 and i < len(arr):
            if W >= arr[i].weight :
                
                profit += arr[i].value
                W -= arr[i].weight
                
            else :
                sm_val = arr[i].value/arr[i].weight
                profit += (W*sm_val)
                W = 0
            
            i += 1
        
        return profit
