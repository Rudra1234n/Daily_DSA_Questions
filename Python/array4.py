class Solution:
	def minJumps(self, arr, n):
	    steps = 0
	    length = len(arr)
	    if len(arr) == 1: return 0
	    if arr[0] == 0: return -1
	    curr = min(arr[0], length - 1)
	    mx = curr
	    for i in range(0, len(arr)):
	        if arr[i] > 0: mx = max(mx, min(arr[i] + i, length - 1))
	        if i == curr:
	            steps += 1
	            if curr == mx and mx != length - 1: return -1
	            curr = mx
	    return -1 if mx != length - 1 else steps
