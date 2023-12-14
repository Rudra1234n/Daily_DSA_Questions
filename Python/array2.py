#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        # code here
        x=(n*(n+1))//2
        s=sum(array)
        return x-s
