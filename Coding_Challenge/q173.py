class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
        arr = sorted(list(set(A)))
        target = B
        sol = []
         
        def find_subsets(arr, target, temp, sol):
            if target == 0:
                sol.append(temp.copy())
                return 
            
            if target < 0:
                return
            
            for i in range(len(arr)):
                if arr[i] > target:
                    break
                    
                temp.append(arr[i])
                find_subsets(arr[i:], target - arr[i], temp, sol)
                temp.pop()
           
        find_subsets(arr, target, [], sol)
        return sol

