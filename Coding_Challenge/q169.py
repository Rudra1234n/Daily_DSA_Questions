class Solution:
	def recreationalSpot(self, arr, n):
		stack=[]
		currmin=arr[0]
		for i in arr[1:]:
		    while stack and i>=stack[-1][0]:
		        stack.pop()
		    if stack and i>stack[-1][1]:
		        return True
		    stack.append([i,currmin])
		    currmin=min(i,currmin)
		return False
