class Solution:

	def print2largest(self,arr, n):
		largest = arr[0]
		second_largest = -1
		
		for i in range(n):
		    if arr[i] > largest:
		        second_largest = largest
		        largest = arr[i]
		    elif arr[i] > second_largest and arr[i] < largest:
		        second_largest = arr[i]
		
		return second_largest
