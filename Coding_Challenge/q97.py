class Solution:

	def kLargest(self,arr, n, k):
        # code here
        arrs=sorted(arr,reverse=True)
        return arrs[0:k]
		# code here
