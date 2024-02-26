class Solution:
    def findExtra(self,a,b,n):
        #add code here
        i = sum(a)-sum(b)
        return a.index(i)
