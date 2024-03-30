class Solution:
	def countStrings(self,n):
    	if n==1:
    	    return 2
    	if n==2:
    	    return 3
    	num1, num2 = 2,3
    	for i in range(3, n+1):
    	    num1, num2 = num2, (num1+num2)%(10**9+7)
    	return num2
