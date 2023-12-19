
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
   def equilibriumPoint(self,A, N):
        if len(A) == 1 : return 1
        cur_total = [A[0]]
        for i in range(1,N):
            cur_total.append(cur_total[-1]+A[i])
        
        for i in range(N):
            if cur_total[-1]-cur_total[i]==cur_total[i-1]:
                return i+1
        
        return -1
