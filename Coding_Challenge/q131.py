class Solution:
    def findSubArrays(self,arr,n):
        cnt = 0
        sum_dict = {0:1}
        prev_sum = 0
        
        for ele in arr:
            prev_sum += ele
        
            if prev_sum in sum_dict:
                cnt += sum_dict[prev_sum]
            
            sum_dict[prev_sum] = sum_dict.get(prev_sum,0)+1
        
        return cnt
