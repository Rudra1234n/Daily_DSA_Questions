#User function Template for python3
class Solution:
	def isPalindrome(self, S):
        # code here
        s=S[::-1]
        if(s==S):
            return 1
        else:
            return 0
