class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
	    dic={}
        max_len=0
        curr_sum=0
        for i in range(n):
            curr_sum+=arr[i]
            if curr_sum==k:
                max_len=max(max_len,i+1)
            rem=curr_sum-k
            if rem in dic:
                max_len=max(max_len,i-dic[rem])
            if curr_sum not in dic:
                dic[curr_sum]=i
        return max_len
